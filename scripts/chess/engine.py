"""
Local Stockfish wrapper: full-game analysis at depth 18, one evaluation per
position (never re-analyzed once cached in the store). See
projects/chess/learning-system-plan.md M1.

Evaluation convention: eval_cp is always stored from White's point of view,
in centipawns. best_move_san / is_best_move / cp_loss describe the move that
was actually played AT this ply, measured against the engine's top choice
from the position before it. Perspective conversion (whose-move-was-it) is
the caller's job -- see detect.py.
"""

import io
import sys
from pathlib import Path

import chess
import chess.engine
import chess.pgn

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402

STOCKFISH_PATH = r"C:\Users\User\OneDrive\Documents\stockfish\stockfish-windows-x86-64-avx2.exe"
DEPTH = 18
THREADS = 3
MATE_SCORE = 100000  # finite stand-in for mate scores, same convention as the retired bi-weekly routine
CP_LOSS_CAP = 1000  # eval magnitudes are clipped to this before diffing for cp_loss, so a move that
# crosses into/out of mate territory doesn't produce a deceptive ~100000 "centipawn loss" -- the full
# eval_cp is still stored uncapped for other uses (is_mate flagging etc.), only cp_loss is affected


def pov(eval_white: int, color: str) -> int:
    """Convert a White-POV eval to the given color's POV."""
    return eval_white if color == "white" else -eval_white


class Engine:
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        self.engine.configure({"Threads": THREADS})

    def close(self):
        self.engine.quit()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def analyse_game(self, pgn_text: str):
        """Returns a list of per-ply dicts covering every move in the game:
        ply, color, move_san, eval_cp (White POV, position after this ply),
        is_mate, best_move_san (engine's top choice from the position before
        this ply), is_best_move, cp_loss (mover's-perspective loss vs best).
        """
        game = chess.pgn.read_game(io.StringIO(pgn_text))
        if game is None:
            return []

        board = game.board()
        node = game
        ply = 0

        info = self.engine.analyse(board, chess.engine.Limit(depth=DEPTH))
        eval_white_prev = info["score"].white().score(mate_score=MATE_SCORE)
        best_move_prev = info.get("pv", [None])[0]

        results = []
        while node.variations:
            next_node = node.variations[0]
            move = next_node.move
            move_san = board.san(move)
            color = "white" if ply % 2 == 0 else "black"

            is_mate = isinstance(info["score"].white(), chess.engine.Mate)
            best_move_san = board.san(best_move_prev) if best_move_prev else None
            is_best = (best_move_prev is not None and move == best_move_prev)

            board.push(move)
            ply += 1

            new_info = self.engine.analyse(board, chess.engine.Limit(depth=DEPTH))
            eval_white_after = new_info["score"].white().score(mate_score=MATE_SCORE)

            capped_prev = max(-CP_LOSS_CAP, min(CP_LOSS_CAP, pov(eval_white_prev, color)))
            capped_after = max(-CP_LOSS_CAP, min(CP_LOSS_CAP, pov(eval_white_after, color)))
            cp_loss = max(0, capped_prev - capped_after)

            results.append({
                "ply": ply,
                "color": color,
                "move_san": move_san,
                "eval_cp": eval_white_after,
                "is_mate": int(is_mate),
                "best_move_san": best_move_san,
                "is_best_move": int(is_best),
                "cp_loss": cp_loss,
            })

            eval_white_prev = eval_white_after
            best_move_prev = new_info.get("pv", [None])[0]
            info = new_info
            node = next_node

        return results


def fen_before_ply(pgn_text: str, ply: int) -> str | None:
    """FEN of the position immediately before the move at `ply` was played --
    i.e. what the mover was actually looking at. ply is 1-indexed, matching
    the moves/evaluations tables (ply 1 = White's first move)."""
    game = chess.pgn.read_game(io.StringIO(pgn_text))
    if game is None:
        return None
    board = game.board()
    node = game
    current = 0
    while node.variations:
        if current == ply - 1:
            return board.fen()
        next_node = node.variations[0]
        board.push(next_node.move)
        current += 1
        node = next_node
    return None


def analyze_and_store(engine: Engine, conn, game_row) -> int:
    """Analyze one game and write its evaluations. Returns ply count analyzed."""
    results = engine.analyse_game(game_row["pgn"])
    if not results:
        return 0
    conn.execute("DELETE FROM evaluations WHERE game_id = ?", (game_row["id"],))
    conn.executemany(
        """
        INSERT INTO evaluations (game_id, ply, eval_cp, is_mate, best_move_san, is_best_move, cp_loss)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (game_row["id"], r["ply"], r["eval_cp"], r["is_mate"],
             r["best_move_san"], r["is_best_move"], r["cp_loss"])
            for r in results
        ],
    )
    conn.commit()
    return len(results)
