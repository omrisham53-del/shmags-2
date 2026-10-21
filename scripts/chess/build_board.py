"""
Bakes drill-set.json into a single self-contained HTML page: no live engine,
no external libraries, no network calls at runtime. Works offline, on bad
wifi, from any device. See projects/chess/learning-system-plan.md M3.

Drill clock: 8 seconds. His own measured per-move time (M0 report) runs
roughly 8-14s/move depending on phase; per rule 4 ("training should be
harder than the game, not easier") this sits at the tight end of that
range deliberately, not at his comfortable average.

Usage:
    python scripts/chess/build_board.py
"""

import json
from pathlib import Path

DRILL_SECONDS = 8
DRILL_SET_PATH = Path(__file__).parent.parent.parent / "projects" / "chess" / "drill-set.json"
OUT_PATH = Path(__file__).parent.parent.parent / "projects" / "chess" / "drill-board.html"

PIECE_UNICODE = {
    "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
    "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚",
}

HTML_TEMPLATE = """<!doctype html>
<title>Chess Drills</title>
<style>
:root {
  --bg: #f5f3ee; --panel: #ffffff; --text: #1a1a1a; --muted: #6b6b6b;
  --board-light: #eeeed2; --board-dark: #769656; --accent: #3b6ea5;
  --correct: #2e7d32; --wrong: #c0392b; --border: #d8d4cb;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #1b1b1b; --panel: #262626; --text: #ececec; --muted: #9a9a9a;
    --board-light: #b9b9a0; --board-dark: #4d6b3a; --accent: #6ea0d8;
    --correct: #4caf50; --wrong: #e57373; --border: #3a3a3a;
  }
}
:root[data-theme="dark"] {
  --bg: #1b1b1b; --panel: #262626; --text: #ececec; --muted: #9a9a9a;
  --board-light: #b9b9a0; --board-dark: #4d6b3a; --accent: #6ea0d8;
  --correct: #4caf50; --wrong: #e57373; --border: #3a3a3a;
}
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--text); font-family: -apple-system, Segoe UI, Roboto, sans-serif;
       display: flex; flex-direction: column; align-items: center; padding: 24px 12px; margin: 0; }
h1 { font-size: 1.1rem; font-weight: 600; margin: 0 0 4px; }
.sub { color: var(--muted); font-size: 0.85rem; margin-bottom: 18px; text-align: center; max-width: 520px; }
.panel { background: var(--panel); border: 1px solid var(--border); border-radius: 12px; padding: 16px;
         max-width: 640px; width: 100%; }
.status-row { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;
              font-size: 0.85rem; color: var(--muted); }
#turnIndicator { font-weight: 700; font-size: 0.95rem; color: var(--text); display: flex; align-items: center; gap: 6px; }
#turnIndicator .dot { width: 11px; height: 11px; border-radius: 50%; display: inline-block;
                       border: 1.5px solid var(--text); }
#turnIndicator .dot.white { background: #f5f5f0; }
#turnIndicator .dot.black { background: #2a2a2a; }
#clock { font-weight: 700; font-size: 1rem; color: var(--text); font-variant-numeric: tabular-nums; }
#clock.low { color: var(--wrong); }
.play-area { display: flex; gap: 16px; align-items: flex-start; }
.board-col { flex: 1; min-width: 0; }
#board { display: grid; grid-template-columns: repeat(8, 1fr); width: 100%; aspect-ratio: 1;
         border: 2px solid var(--border); border-radius: 6px; overflow: hidden; }
.sq { display: flex; align-items: center; justify-content: center; font-size: clamp(20px, 6vw, 40px);
      cursor: pointer; user-select: none; position: relative; aspect-ratio: 1; line-height: 1; }
.sq.light { background: var(--board-light); }
.sq.dark { background: var(--board-dark); }
.sq.selected { outline: 3px solid var(--accent); outline-offset: -3px; z-index: 1; }
.piece-white { color: #f7f5ef; -webkit-text-stroke: 1.3px #26251f; text-stroke: 1.3px #26251f;
               paint-order: stroke fill; }
.piece-black { color: #1b1a17; -webkit-text-stroke: 0.6px #1b1a17; text-stroke: 0.6px #1b1a17; }
.button-col { display: flex; flex-direction: column; gap: 8px; width: 150px; flex-shrink: 0; }
button { background: var(--accent); color: white; border: none; border-radius: 8px; padding: 12px 10px;
         font-size: 0.85rem; cursor: pointer; width: 100%; }
button.secondary { background: transparent; color: var(--muted); border: 1px solid var(--border); }
button:disabled { opacity: 0.4; cursor: default; }
#feedback { margin-top: 12px; padding: 10px; border-radius: 8px; font-size: 0.9rem; display: none; }
#feedback.correct { background: color-mix(in srgb, var(--correct) 15%, transparent); color: var(--correct); display: block; }
#feedback.wrong { background: color-mix(in srgb, var(--wrong) 15%, transparent); color: var(--wrong); display: block; }
#summary { display: none; text-align: center; }
#summary table { width: 100%; margin: 12px 0; font-size: 0.9rem; }
#summary td { padding: 4px 0; }
#summary td:last-child { text-align: right; font-weight: 600; }
@media (max-width: 560px) {
  .play-area { flex-direction: column; }
  .button-col { flex-direction: row; width: 100%; }
}
</style>

<h1>Chess Drills</h1>
<div class="sub">Commit a move before you see anything. No position tells you whether it's winning,\
 losing, or equal -- that's the point.</div>

<div class="panel">
  <div id="quiz">
    <div class="status-row">
      <span id="counter">Drill 1 / N</span>
      <span id="turnIndicator"></span>
      <span id="clock">8</span>
    </div>
    <div class="play-area">
      <div class="board-col">
        <div id="board"></div>
        <div id="feedback"></div>
      </div>
      <div class="button-col">
        <button class="secondary" id="skipBtn">Don't know / skip</button>
        <button id="nextBtn" disabled>Next drill</button>
      </div>
    </div>
  </div>
  <div id="summary">
    <h2 style="margin:0 0 8px;font-size:1rem;">Session done</h2>
    <table id="summaryTable"></table>
    <button id="restartBtn">Run again</button>
  </div>
</div>

<script>
const DRILLS = __DRILLS_JSON__;
const DRILL_SECONDS = __DRILL_SECONDS__;

let order = [];
let idx = 0;
let selected = null;
let timer = null;
let timeLeft = DRILL_SECONDS;
let committed = false;
let results = []; // {source, correct}

function shuffledOrder(n) {
  const a = Array.from({length: n}, (_, i) => i);
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function parseFen(fen) {
  const [placement, active] = fen.split(" ");
  const rows = placement.split("/");
  const grid = {}; // "e4" -> piece char
  const files = "abcdefgh";
  for (let r = 0; r < 8; r++) {
    let f = 0;
    for (const ch of rows[r]) {
      if (/\\d/.test(ch)) { f += parseInt(ch, 10); }
      else { grid[files[f] + (8 - r)] = ch; f += 1; }
    }
  }
  return { grid, active };
}

let currentGrid = null;
let boardOrientation = "w";

function renderGrid(grid) {
  const files = "abcdefgh";
  const boardEl = document.getElementById("board");
  boardEl.innerHTML = "";
  const ranks = boardOrientation === "w" ? [8,7,6,5,4,3,2,1] : [1,2,3,4,5,6,7,8];
  const fileOrder = boardOrientation === "w" ? files.split("") : files.split("").reverse();
  for (const rank of ranks) {
    for (const file of fileOrder) {
      const sq = file + rank;
      const div = document.createElement("div");
      const isLight = (files.indexOf(file) + rank) % 2 === 1;
      div.className = "sq " + (isLight ? "light" : "dark");
      div.dataset.sq = sq;
      const piece = grid[sq];
      if (piece) {
        div.textContent = PIECE_UNICODE[piece] || "";
        div.classList.add(piece === piece.toUpperCase() ? "piece-white" : "piece-black");
      }
      div.addEventListener("click", onSquareClick);
      boardEl.appendChild(div);
    }
  }
}

function updateTurnIndicator(active) {
  const el = document.getElementById("turnIndicator");
  const label = active === "w" ? "White to move" : "Black to move";
  const dotClass = active === "w" ? "white" : "black";
  el.innerHTML = `<span class="dot ${dotClass}"></span>${label}`;
}

function renderBoard(fen) {
  const { grid, active } = parseFen(fen);
  currentGrid = grid;
  boardOrientation = active; // orient so the side to move is at the bottom
  renderGrid(currentGrid);
  updateTurnIndicator(active);
  return active;
}

// Minimal move applier: enough to correctly show captures, promotion, castling,
// and en passant for the purpose of revealing what the correct move looked like.
function applyMove(grid, uci) {
  const g = Object.assign({}, grid);
  const from = uci.slice(0, 2);
  const to = uci.slice(2, 4);
  const promo = uci.length > 4 ? uci[4] : null;
  let piece = g[from];
  delete g[from];
  if (!piece) return g; // defensive: shouldn't happen with well-formed drill data
  const isPawn = piece.toLowerCase() === "p";
  if (isPawn && from[0] !== to[0] && !grid[to]) {
    // en passant: captured pawn sits on the from-rank, to-file
    delete g[to[0] + from[1]];
  }
  if (promo) {
    piece = piece === piece.toUpperCase() ? promo.toUpperCase() : promo.toLowerCase();
  }
  if (piece.toLowerCase() === "k" && Math.abs(from.charCodeAt(0) - to.charCodeAt(0)) === 2) {
    const rank = from[1];
    if (to[0] === "g") { g["f" + rank] = g["h" + rank]; delete g["h" + rank]; }
    else if (to[0] === "c") { g["d" + rank] = g["a" + rank]; delete g["a" + rank]; }
  }
  g[to] = piece;
  return g;
}

const PIECE_UNICODE = __PIECE_UNICODE_JSON__;

function onSquareClick(e) {
  if (committed) return;
  const sq = e.currentTarget.dataset.sq;
  if (!selected) {
    if (!e.currentTarget.textContent) return; // clicked an empty square first
    selected = sq;
    e.currentTarget.classList.add("selected");
    return;
  }
  const from = selected;
  const to = sq;
  document.querySelectorAll(".sq.selected").forEach(el => el.classList.remove("selected"));
  selected = null;
  commitMove(from + to);
}

function commitMove(uci) {
  if (committed) return;
  committed = true;
  clearInterval(timer);
  const drill = DRILLS[order[idx]];
  const correct = drill.correct_move_uci.slice(0, 4);
  const isRight = uci === correct;
  renderGrid(applyMove(currentGrid, drill.correct_move_uci));
  showFeedback(isRight, drill);
  results.push({ source: drill.source, correct: isRight });
}

function skip() {
  if (committed) return;
  committed = true;
  clearInterval(timer);
  const drill = DRILLS[order[idx]];
  renderGrid(applyMove(currentGrid, drill.correct_move_uci));
  showFeedback(false, drill, true);
  results.push({ source: drill.source, correct: false });
}

function showFeedback(isRight, drill, skipped) {
  const fb = document.getElementById("feedback");
  fb.className = isRight ? "correct" : "wrong";
  const correctSan = drill.correct_move_san ? drill.correct_move_san : drill.correct_move_uci;
  fb.textContent = skipped
    ? `Skipped. The move was ${correctSan}.`
    : (isRight ? `Right -- ${correctSan}.` : `Not quite. The move was ${correctSan}.`);
  document.getElementById("nextBtn").disabled = false;
}

function startTimer() {
  timeLeft = DRILL_SECONDS;
  updateClock();
  timer = setInterval(() => {
    timeLeft -= 1;
    updateClock();
    if (timeLeft <= 0) {
      clearInterval(timer);
      if (!committed) skip();
    }
  }, 1000);
}

function updateClock() {
  const el = document.getElementById("clock");
  el.textContent = timeLeft;
  el.classList.toggle("low", timeLeft <= 3);
}

function loadDrill() {
  committed = false;
  selected = null;
  document.getElementById("feedback").className = "";
  document.getElementById("feedback").textContent = "";
  document.getElementById("nextBtn").disabled = true;
  document.getElementById("counter").textContent = `Drill ${idx + 1} / ${order.length}`;
  const drill = DRILLS[order[idx]];
  renderBoard(drill.fen);
  startTimer();
}

function nextDrill() {
  idx += 1;
  if (idx >= order.length) {
    showSummary();
  } else {
    loadDrill();
  }
}

function showSummary() {
  document.getElementById("quiz").style.display = "none";
  const summary = document.getElementById("summary");
  summary.style.display = "block";
  const bySource = {};
  for (const r of results) {
    bySource[r.source] = bySource[r.source] || { correct: 0, total: 0 };
    bySource[r.source].total += 1;
    if (r.correct) bySource[r.source].correct += 1;
  }
  const labels = { own_blunder: "Your past blunders", own_null: "Your quiet positions", lichess_puzzle: "Puzzle pool" };
  const total = results.length;
  const totalCorrect = results.filter(r => r.correct).length;
  let rows = `<tr><td><strong>Overall</strong></td><td>${totalCorrect} / ${total}</td></tr>`;
  for (const [src, v] of Object.entries(bySource)) {
    rows += `<tr><td>${labels[src] || src}</td><td>${v.correct} / ${v.total}</td></tr>`;
  }
  document.getElementById("summaryTable").innerHTML = rows;
}

function start() {
  order = shuffledOrder(DRILLS.length);
  idx = 0;
  results = [];
  document.getElementById("quiz").style.display = "block";
  document.getElementById("summary").style.display = "none";
  loadDrill();
}

document.getElementById("skipBtn").addEventListener("click", skip);
document.getElementById("nextBtn").addEventListener("click", nextDrill);
document.getElementById("restartBtn").addEventListener("click", start);
start();
</script>
"""


def main():
    drills = json.loads(DRILL_SET_PATH.read_text(encoding="utf-8"))
    html = (
        HTML_TEMPLATE
        .replace("__DRILLS_JSON__", json.dumps(drills))
        .replace("__DRILL_SECONDS__", str(DRILL_SECONDS))
        .replace("__PIECE_UNICODE_JSON__", json.dumps(PIECE_UNICODE))
    )
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"Built {OUT_PATH} ({len(drills)} drills baked in, {OUT_PATH.stat().st_size / 1024:.0f} KB).")


if __name__ == "__main__":
    main()
