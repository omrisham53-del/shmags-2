"""
M5 position-pattern matcher: back-searches the whole archive for positions
where a studied concept was actually live, then shows what he did about it.
See projects/chess/learning-system-plan.md M5.

The point is the sequence, chapter first and then the games. The concept
supplies the lens; this script finds every position in his own play where
that lens applies and reports his real response. Without it the Rozman book
is the one input in the system not generated from his own games, and so the
most likely to become dead weight.

Each pattern answers two questions, and the second is the one that matters:

  1. Did the structural condition hold here?
  2. What did he actually do about it over the following moves?

A matcher that only answered the first would produce "this came up 40 times"
and teach nothing.

Every report also carries a blunder overlay, because of the 2026-11-02 M4
finding: about 96% of his lead-losing sequences contain a discrete blunder
rather than gradual drift. So for each match the report says whether a real
cliff landed inside the window where the concept was live. "The concept
applied and you blundered right there" is a sharper signal than either fact
alone.

Usage:
    python scripts/chess/patterns.py --list
    python scripts/chess/patterns.py --pattern opposite_castling
    python scripts/chess/patterns.py --pattern open_file_unclaimed --limit 8
    python scripts/chess/patterns.py --log "Chapter 4: opposite castling means race, do not defend"
"""

import argparse
import io
import sys
from datetime import date
from pathlib import Path

import chess
import chess.pgn

sys.path.insert(0, str(Path(__file__).parent))

import store
from detect import CLIFF_THRESHOLD, _game_trajectory

CONCEPT_LOG = Path(__file__).resolve().parents[2] / "projects" / "chess" / "concept-log.md"

RESPONSE_WINDOW = 12  # plies to watch after a match, to judge what he did
MIN_PLY = 12          # below this it is still opening theory, not a decision


# --------------------------------------------------------------------------
# Board replay
# --------------------------------------------------------------------------

def replay(pgn_text):
    """Yield (ply, board_before_move, move) for every move in the game.

    One pass per game. `fen_before_ply` re-parses the whole PGN per call,
    which is fine for a handful of positions and far too slow for scanning
    every ply of every game.
    """
    game = chess.pgn.read_game(io.StringIO(pgn_text))
    if game is None:
        return
    board = game.board()
    node = game
    ply = 0
    while node.variations:
        nxt = node.variations[0]
        ply += 1
        yield ply, board.copy(stack=False), nxt.move
        board.push(nxt.move)
        node = nxt


def _my_side(game_row):
    return chess.WHITE if game_row["my_color"] == "white" else chess.BLACK


# --------------------------------------------------------------------------
# Structural helpers
# --------------------------------------------------------------------------

def _king_wing(board, color):
    """'queenside' / 'kingside' / 'centre' for a king's file."""
    sq = board.king(color)
    if sq is None:
        return None
    f = chess.square_file(sq)
    if f <= 2:
        return "queenside"
    if f >= 5:
        return "kingside"
    return "centre"


def _open_files(board):
    """Files with no pawns of either colour."""
    out = []
    for f in range(8):
        has_pawn = any(
            (p := board.piece_at(chess.square(f, r))) and p.piece_type == chess.PAWN
            for r in range(8)
        )
        if not has_pawn:
            out.append(f)
    return out


def _pawn_files(board, color):
    return {
        chess.square_file(sq)
        for sq in board.pieces(chess.PAWN, color)
    }


def _isolated_pawns(board, color):
    files = _pawn_files(board, color)
    return {f for f in files if (f - 1) not in files and (f + 1) not in files}


def _passed_pawns(board, color):
    out = []
    enemy = not color
    enemy_pawn_sqs = board.pieces(chess.PAWN, enemy)
    for sq in board.pieces(chess.PAWN, color):
        f, r = chess.square_file(sq), chess.square_rank(sq)
        blocked = False
        for ef in (f - 1, f, f + 1):
            if not 0 <= ef <= 7:
                continue
            for esq in enemy_pawn_sqs:
                if chess.square_file(esq) != ef:
                    continue
                er = chess.square_rank(esq)
                ahead = er > r if color == chess.WHITE else er < r
                if ahead:
                    blocked = True
                    break
            if blocked:
                break
        if not blocked:
            out.append(sq)
    return out


def _pawn_advances_toward(moves_after, board_at_match, color, target_wing):
    """Did he push pawns on the given wing in the window after the match?"""
    count = 0
    for _, b, mv in moves_after:
        piece = b.piece_at(mv.from_square)
        if piece is None or piece.color != color or piece.piece_type != chess.PAWN:
            continue
        f = chess.square_file(mv.to_square)
        wing = "queenside" if f <= 2 else ("kingside" if f >= 5 else "centre")
        if wing == target_wing:
            count += 1
    return count


# --------------------------------------------------------------------------
# Patterns
# --------------------------------------------------------------------------
# Each pattern is a dict:
#   match(board, me)        -> bool, does the structural condition hold
#   respond(window, board, me) -> (verdict, detail) describing what he did

def _m_opposite_castling(board, me, ctx):
    """Both sides have genuinely CASTLED, on opposite wings.

    Deliberately driven by real castling moves recorded during replay, not by
    which file each king happens to sit on. The file-based version matched
    endgames where two kings had simply wandered to opposite wings, which
    produced nonsense like a move-58 "opposite castling" hit in a king-and-pawn
    ending, where "push pawns at their king" is not the lens at all.
    """
    mine = ctx["castled"].get(me)
    theirs = ctx["castled"].get(not me)
    if mine is None or theirs is None:
        return False
    return mine != theirs


def _r_opposite_castling(window, board, me):
    theirs = _king_wing(board, not me)
    pushes = _pawn_advances_toward(window, board, me, theirs)
    if pushes >= 2:
        return "attacked", "{} pawn pushes toward their king".format(pushes)
    if pushes == 1:
        return "hesitant", "1 pawn push toward their king"
    return "never started", "no pawn pushes toward their king in {} plies".format(len(window))


def _m_open_file_unclaimed(board, me, ctx):
    files = _open_files(board)
    if not files:
        return False
    rooks = board.pieces(chess.ROOK, me)
    if not rooks:
        return False
    # an open file exists and none of my rooks is on it
    return not any(chess.square_file(sq) in files for sq in rooks)


def _r_open_file_unclaimed(window, board, me):
    files = set(_open_files(board))
    for _, b, mv in window:
        piece = b.piece_at(mv.from_square)
        if piece and piece.color == me and piece.piece_type == chess.ROOK:
            if chess.square_file(mv.to_square) in files:
                return "claimed", "rook to the open file"
    return "never claimed", "no rook reached the open file in {} plies".format(len(window))


def _m_their_isolated_pawn(board, me, ctx):
    return bool(_isolated_pawns(board, not me))


def _r_their_isolated_pawn(window, board, me):
    iso = _isolated_pawns(board, not me)
    targets = set()
    for sq in board.pieces(chess.PAWN, not me):
        if chess.square_file(sq) in iso:
            targets.add(sq)
    for _, b, mv in window:
        piece = b.piece_at(mv.from_square)
        if piece and piece.color == me and mv.to_square in targets:
            return "pressured", "captured or attacked the isolated pawn"
        if piece and piece.color == me and piece.piece_type != chess.PAWN:
            # occupying the square directly in front of an isolated pawn
            for t in targets:
                front = t + (8 if (not me) == chess.WHITE else -8)
                if mv.to_square == front:
                    return "blockaded", "piece in front of the isolated pawn"
    return "ignored", "never pressured or blockaded it in {} plies".format(len(window))


def _m_my_passed_pawn(board, me, ctx):
    return bool(_passed_pawns(board, me))


def _r_my_passed_pawn(window, board, me):
    passers = set(_passed_pawns(board, me))
    for _, b, mv in window:
        piece = b.piece_at(mv.from_square)
        if piece and piece.color == me and piece.piece_type == chess.PAWN:
            if mv.from_square in passers:
                return "pushed", "advanced the passed pawn"
            passers = {p for p in passers if p != mv.from_square}
    return "left it", "never advanced the passed pawn in {} plies".format(len(window))


def _m_their_king_uncastled(board, me, ctx):
    if board.fullmove_number < 10:
        return False
    enemy = not me
    start = chess.E1 if enemy == chess.WHITE else chess.E8
    return board.king(enemy) == start and _king_wing(board, enemy) == "centre"


def _r_their_king_uncastled(window, board, me):
    opens = 0
    for _, b, mv in window:
        piece = b.piece_at(mv.from_square)
        if piece is None or piece.color != me:
            continue
        f = chess.square_file(mv.to_square)
        if 2 <= f <= 5 and (b.is_capture(mv) or piece.piece_type == chess.PAWN):
            opens += 1
    if opens >= 2:
        return "opened the centre", "{} central captures or pawn moves".format(opens)
    return "let them consolidate", "little central action in {} plies".format(len(window))


PATTERNS = {
    "opposite_castling": {
        "description": "Both kings castled on opposite wings. The lens: this is a race, so push pawns at their king.",
        "match": _m_opposite_castling,
        "respond": _r_opposite_castling,
        "good": {"attacked"},
    },
    "open_file_unclaimed": {
        "description": "A fully open file exists and none of your rooks is on it.",
        "match": _m_open_file_unclaimed,
        "respond": _r_open_file_unclaimed,
        "good": {"claimed"},
    },
    "their_isolated_pawn": {
        "description": "Your opponent has an isolated pawn. The lens: blockade the square in front, then attack it.",
        "match": _m_their_isolated_pawn,
        "respond": _r_their_isolated_pawn,
        "good": {"pressured", "blockaded"},
    },
    "my_passed_pawn": {
        "description": "You have a passed pawn. The lens: passed pawns must be pushed.",
        "match": _m_my_passed_pawn,
        "respond": _r_my_passed_pawn,
        "good": {"pushed"},
    },
    "their_king_uncastled": {
        "description": "Their king is still on its start square past move 10. The lens: open the centre before they fix it.",
        "match": _m_their_king_uncastled,
        "respond": _r_their_king_uncastled,
        "good": {"opened the centre"},
    },
}


# --------------------------------------------------------------------------
# Search
# --------------------------------------------------------------------------

def search(conn, pattern_name, time_class="rapid", time_control="600"):
    spec = PATTERNS[pattern_name]
    games = [
        g for g in store.get_games(conn, time_class=time_class, time_control=time_control)
        if g["my_color"]
    ]

    hits = []
    for g in games:
        traj = {r["ply"]: r for r in _game_trajectory(conn, g)}
        if not traj:
            continue  # unanalyzed game: no evals, so no blunder overlay
        me = _my_side(g)

        frames = list(replay(g["pgn"]))
        by_ply = {p: (b, mv) for p, b, mv in frames}

        # Castling state is accumulated as the game is walked, so a matcher
        # can ask "has this side actually castled, and which way" rather than
        # inferring it from where a king happens to be sitting.
        ctx = {"castled": {}}
        matched_ply = None
        for ply, board, mv in frames:
            if ply >= MIN_PLY and board.turn == me and spec["match"](board, me, ctx):
                matched_ply = ply
                break  # first occurrence per game, so one game is one data point
            if board.is_castling(mv):
                side = "kingside" if chess.square_file(mv.to_square) > 4 else "queenside"
                ctx["castled"][board.turn] = side

        if matched_ply is None:
            continue

        board = by_ply[matched_ply][0]
        window = [(p, b, mv) for p, b, mv in frames
                  if matched_ply <= p < matched_ply + RESPONSE_WINDOW]
        verdict, detail = spec["respond"](window, board, me)

        # Blunder overlay: did a real cliff land while the concept was live?
        worst, worst_ply = 0, None
        for p, _b, _mv in window:
            row = traj.get(p)
            if row and row["is_mine"] and row["cp_loss"] and row["cp_loss"] > worst:
                worst, worst_ply = row["cp_loss"], p

        hits.append({
            "game_id": g["id"], "url": g["url"], "end_date": g["end_date"],
            "my_result": g["my_result"], "my_color": g["my_color"],
            "ply": matched_ply, "verdict": verdict, "detail": detail,
            "good": verdict in spec["good"],
            "worst_cp_loss": worst, "worst_ply": worst_ply,
            "blundered": worst >= CLIFF_THRESHOLD,
        })

    return hits


def report(pattern_name, hits, limit):
    spec = PATTERNS[pattern_name]
    print("\n{}".format("=" * 68))
    print("Pattern: {}".format(pattern_name))
    print(spec["description"])
    print("=" * 68)

    if not hits:
        print("\nNo games in the archive match this pattern yet.")
        return

    good = [h for h in hits if h["good"]]
    bad = [h for h in hits if not h["good"]]
    blundered = [h for h in hits if h["blundered"]]

    print("\n{} of your games reached this position type.".format(len(hits)))
    print("  Played it the way the concept says: {}".format(len(good)))
    print("  Did not: {}".format(len(bad)))
    print("  A real blunder (>= {}cp) landed while the concept was live: {}".format(
        CLIFF_THRESHOLD, len(blundered)))

    # Lead with the ones he got wrong: that is where the reading pays off.
    ordered = bad + good
    print("\n{}".format("-" * 68))
    for h in ordered[:limit]:
        mark = "ok  " if h["good"] else "MISS"
        line = "{}  move {:>3}  {}  {:<4}  {}".format(
            mark, (h["ply"] + 1) // 2, h["end_date"], h["my_result"], h["detail"])
        print(line)
        if h["blundered"]:
            # detect.py clips cp_loss at 2000, so that exact value is a clamp
            # rather than a measurement. Reporting it as a precise number would
            # be a false reading of a mate-score artifact.
            mv_no = (h["worst_ply"] + 1) // 2
            if h["worst_cp_loss"] >= 2000:
                print("      and you threw the game away at move {} in the same window".format(mv_no))
            else:
                print("      and you dropped {}cp at move {} in the same window".format(
                    h["worst_cp_loss"], mv_no))
        print("      {}".format(h["url"]))
    if len(ordered) > limit:
        print("\n({} more, raise --limit to see them)".format(len(ordered) - limit))


def log_concept(text, pattern):
    CONCEPT_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not CONCEPT_LOG.exists():
        header = (
            "# Concept Log\n\n"
            "One entry per studied chapter of Rozman's *How to Win at Chess: Intermediate*, "
            "in Omri's own words. Read the book in order: it is a sequenced curriculum and "
            "skipping around breaks concepts that depend on earlier ones.\n\n"
            "Each entry names the `patterns.py` pattern that back-searches the archive for it, "
            "so the concept gets tested against his own games rather than just read. "
            "Entries without a pattern are concepts the matcher cannot express yet.\n\n"
            "---\n\n"
        )
        CONCEPT_LOG.write_text(header, encoding="utf-8")

    with CONCEPT_LOG.open("a", encoding="utf-8") as fh:
        fh.write("## {}\n\n{}\n\n".format(date.today().isoformat(), text))
        if pattern:
            fh.write("Pattern: `{}`\n\n".format(pattern))
            fh.write("    python scripts/chess/patterns.py --pattern {}\n\n".format(pattern))
        else:
            fh.write("Pattern: none yet.\n\n")
    print("Logged to {}".format(CONCEPT_LOG))


def main():
    ap = argparse.ArgumentParser(description="M5 concept log and position-pattern matcher")
    ap.add_argument("--list", action="store_true", help="show available patterns")
    ap.add_argument("--pattern", help="pattern to back-search the archive for")
    ap.add_argument("--all", action="store_true", help="run every pattern, summary only")
    ap.add_argument("--limit", type=int, default=10, help="games to show per pattern")
    ap.add_argument("--log", help="append a concept entry in your own words")
    args = ap.parse_args()

    if args.log:
        log_concept(args.log, args.pattern)
        return

    if args.list or not (args.pattern or args.all):
        print("\nAvailable patterns:\n")
        for name, spec in PATTERNS.items():
            print("  {:22s} {}".format(name, spec["description"]))
        print("\n  python scripts/chess/patterns.py --pattern <name>")
        return

    conn = store.init_db()

    if args.all:
        print("\n{:22s} {:>7} {:>7} {:>7} {:>10}".format(
            "pattern", "games", "played", "missed", "blundered"))
        print("-" * 58)
        for name in PATTERNS:
            hits = search(conn, name)
            good = sum(1 for h in hits if h["good"])
            bl = sum(1 for h in hits if h["blundered"])
            print("{:22s} {:>7} {:>7} {:>7} {:>10}".format(
                name, len(hits), good, len(hits) - good, bl))
        return

    if args.pattern not in PATTERNS:
        print("Unknown pattern: {}".format(args.pattern))
        print("Known: {}".format(", ".join(PATTERNS)))
        return

    hits = search(conn, args.pattern)
    report(args.pattern, hits, args.limit)


if __name__ == "__main__":
    main()
