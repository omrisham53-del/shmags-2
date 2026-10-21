"""
Local SQLite store for the chess learning system. Everything downstream
(fetch, clock analysis, engine detectors, drills) reads and writes through
this -- see projects/chess/learning-system-plan.md M0.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "chess.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL,
    pgn TEXT NOT NULL,
    white TEXT,
    black TEXT,
    white_elo INTEGER,
    black_elo INTEGER,
    my_color TEXT,       -- 'white' or 'black'
    my_rating INTEGER,
    opp_rating INTEGER,
    result TEXT,         -- raw PGN Result header, e.g. '1-0'
    my_result TEXT,       -- 'win' / 'loss' / 'draw' from my_color's perspective
    termination TEXT,
    time_class TEXT,
    time_control TEXT,
    end_date TEXT,        -- UTCDate header, YYYY.MM.DD
    end_time TEXT,
    ply_count INTEGER,
    clock_parsed INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS moves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL REFERENCES games(id) ON DELETE CASCADE,
    ply INTEGER NOT NULL,
    color TEXT NOT NULL,          -- 'white' or 'black'
    move_san TEXT NOT NULL,
    clock_seconds REAL,           -- time remaining after this move
    time_spent REAL,              -- seconds spent on this move
    phase TEXT,                   -- 'opening' / 'middlegame' / 'endgame'
    UNIQUE(game_id, ply)
);

-- M1: engine evaluations, one row per ply once analyzed
CREATE TABLE IF NOT EXISTS evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL REFERENCES games(id) ON DELETE CASCADE,
    ply INTEGER NOT NULL,
    eval_cp INTEGER,           -- centipawns, from the side to move's perspective
    is_mate INTEGER DEFAULT 0, -- 1 if eval_cp is actually a mate-in-N encoded score
    best_move_san TEXT,
    is_best_move INTEGER,      -- 1 if the move played matched the engine's best move
    cp_loss INTEGER,           -- eval drop vs the best move, this ply
    UNIQUE(game_id, ply)
);

-- M2: self-review guesses, logged before engine output is seen
CREATE TABLE IF NOT EXISTS annotations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL REFERENCES games(id) ON DELETE CASCADE,
    ply INTEGER,
    note TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- M3: drill history
CREATE TABLE IF NOT EXISTS drills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fen TEXT NOT NULL,
    source TEXT,              -- 'own_blunder' / 'own_null' / 'lichess_puzzle'
    source_game_id INTEGER REFERENCES games(id),
    correct_move_san TEXT,
    shown_at TEXT,
    user_move_san TEXT,
    correct INTEGER,
    time_taken_seconds REAL
);
"""


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _migrate(conn):
    """Add columns that postdate the original schema, without disturbing existing data."""
    cols = {row["name"] for row in conn.execute("PRAGMA table_info(games)")}
    if "reviewed_at" not in cols:
        conn.execute("ALTER TABLE games ADD COLUMN reviewed_at TEXT")
        conn.commit()


def init_db():
    conn = get_conn()
    conn.executescript(SCHEMA)
    conn.commit()
    _migrate(conn)
    return conn


def games_needing_review(conn, time_class="rapid", time_control="600"):
    """Games never through /chess-review, oldest first (review them in the order played)."""
    return conn.execute(
        """
        SELECT * FROM games
        WHERE time_class = ? AND time_control = ? AND reviewed_at IS NULL
        ORDER BY end_date ASC, end_time ASC
        """,
        (time_class, time_control),
    ).fetchall()


def mark_reviewed(conn, game_ids):
    import datetime
    now = datetime.datetime.utcnow().isoformat()
    conn.executemany(
        "UPDATE games SET reviewed_at = ? WHERE id = ?",
        [(now, gid) for gid in game_ids],
    )
    conn.commit()


def known_urls(conn):
    return {row["url"] for row in conn.execute("SELECT url FROM games")}


def insert_game(conn, game: dict) -> int:
    """Insert a game if its url isn't already stored. Returns the row id either way."""
    existing = conn.execute(
        "SELECT id FROM games WHERE url = ?", (game["url"],)
    ).fetchone()
    if existing:
        return existing["id"]

    cur = conn.execute(
        """
        INSERT INTO games (
            url, pgn, white, black, white_elo, black_elo,
            my_color, my_rating, opp_rating, result, my_result, termination,
            time_class, time_control, end_date, end_time, ply_count
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            game["url"], game["pgn"], game.get("white"), game.get("black"),
            game.get("white_elo"), game.get("black_elo"),
            game.get("my_color"), game.get("my_rating"), game.get("opp_rating"),
            game.get("result"), game.get("my_result"), game.get("termination"),
            game.get("time_class"), game.get("time_control"),
            game.get("end_date"), game.get("end_time"), game.get("ply_count"),
        ),
    )
    conn.commit()
    return cur.lastrowid


def games_needing_clock_parse(conn, time_class="rapid", time_control="600"):
    return conn.execute(
        "SELECT * FROM games WHERE clock_parsed = 0 AND time_class = ? AND time_control = ?",
        (time_class, time_control),
    ).fetchall()


def replace_moves(conn, game_id: int, moves: list):
    conn.execute("DELETE FROM moves WHERE game_id = ?", (game_id,))
    conn.executemany(
        """
        INSERT INTO moves (game_id, ply, color, move_san, clock_seconds, time_spent, phase)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (game_id, m["ply"], m["color"], m["move_san"], m["clock_seconds"],
             m["time_spent"], m["phase"])
            for m in moves
        ],
    )
    conn.execute("UPDATE games SET clock_parsed = 1 WHERE id = ?", (game_id,))
    conn.commit()


def games_needing_evaluation(conn, time_class="rapid", time_control="600", since_date=None):
    """Games with no evaluations rows yet, newest first. since_date is an
    inclusive 'YYYY-MM-DD' floor on games.end_date."""
    q = """
        SELECT g.* FROM games g
        WHERE g.time_class = ? AND g.time_control = ?
          AND NOT EXISTS (SELECT 1 FROM evaluations e WHERE e.game_id = g.id)
    """
    params = [time_class, time_control]
    if since_date:
        q += " AND g.end_date >= ?"
        params.append(since_date)
    q += " ORDER BY g.end_date DESC, g.end_time DESC"
    return conn.execute(q, params).fetchall()


def get_games(conn, time_class=None, time_control=None):
    q = "SELECT * FROM games"
    params = []
    conds = []
    if time_class:
        conds.append("time_class = ?")
        params.append(time_class)
    if time_control:
        conds.append("time_control = ?")
        params.append(time_control)
    if conds:
        q += " WHERE " + " AND ".join(conds)
    return conn.execute(q, params).fetchall()


def get_moves(conn, game_id: int, color=None):
    if color:
        return conn.execute(
            "SELECT * FROM moves WHERE game_id = ? AND color = ? ORDER BY ply",
            (game_id, color),
        ).fetchall()
    return conn.execute(
        "SELECT * FROM moves WHERE game_id = ? ORDER BY ply", (game_id,)
    ).fetchall()


if __name__ == "__main__":
    conn = init_db()
    n = conn.execute("SELECT COUNT(*) AS n FROM games").fetchone()["n"]
    print(f"DB ready at {DB_PATH} -- {n} games stored.")
