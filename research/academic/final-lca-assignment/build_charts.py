# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

OUT = r"c:\עמרי\Shmags 2\research\academic\final-lca-assignment\charts"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#c3c2b7"
plt.rcParams["text.color"] = "#0b0b0b"
plt.rcParams["axes.labelcolor"] = "#0b0b0b"
plt.rcParams["xtick.color"] = "#52514e"
plt.rcParams["ytick.color"] = "#52514e"

BLUE = "#2a78d6"      # Interbeton (categorical slot 1)
GREEN = "#008300"     # JSW (categorical slot 2)
ORANGE = "#eb6834"    # highlight (focal companies in market-cap charts)
GRAY = "#c9c8c2"      # context / muted slices
GRID = "#e1e0d9"
INK = "#0b0b0b"
MUTED = "#898781"

# ---------------------------------------------------------------------------
# 1. Manufacturing process flowchart (with manufacturing vs construction-stage
#    grouping, since placement/hardening is a construction-stage step, not
#    manufacturing)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.2, 3.1), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 2.7)
ax.axis("off")

steps = [
    "Raw material\nextraction\n(limestone, clay,\nsand, gravel)",
    "Cement\nproduction\n(kiln calcination\n+ grinding)",
    "Batching at\nready-mix plant\n(weigh + mix\ncement, aggregate,\nwater, admixtures)",
    "Transport\n(truck-mounted\nmixer to site)",
    "Placement &\nhardening\n(pour, compact,\ncement hydration)",
]
n = len(steps)
box_w, box_h = 1.7, 1.5
gap = 0.35
total_w = n * box_w + (n - 1) * gap
x0 = (10 - total_w) / 2
y0 = 0.25

for i, label in enumerate(steps):
    x = x0 + i * (box_w + gap)
    box = FancyBboxPatch((x, y0), box_w, box_h,
                          boxstyle="round,pad=0.04,rounding_size=0.08",
                          linewidth=1.3, edgecolor=BLUE, facecolor="#eef4fc")
    ax.add_patch(box)
    ax.text(x + box_w / 2, y0 + box_h / 2, label, ha="center", va="center",
             fontsize=8.3, color=INK, linespacing=1.35)
    if i < n - 1:
        arr = FancyArrowPatch((x + box_w + 0.03, y0 + box_h / 2),
                               (x + box_w + gap - 0.03, y0 + box_h / 2),
                               arrowstyle="-|>", mutation_scale=14,
                               linewidth=1.4, color=MUTED)
        ax.add_patch(arr)

# grouping brackets: steps 1-3 = manufacturing (A1-A3, product stage);
# steps 4-5 = construction stage (A4-A5), not manufacturing
def group_box(first_i, last_i, label, color):
    x_start = x0 + first_i * (box_w + gap)
    x_end = x0 + last_i * (box_w + gap) + box_w
    width = x_end - x_start
    y = y0 + box_h + 0.22
    grp = FancyBboxPatch((x_start, y), width, 0.4,
                          boxstyle="round,pad=0.02,rounding_size=0.06",
                          linewidth=1.0, edgecolor=color, facecolor="none")
    ax.add_patch(grp)
    ax.text(x_start + width / 2, y + 0.2, label, ha="center", va="center",
            fontsize=8.3, color=color, fontweight="bold")

group_box(0, 2, "Manufacturing (A1-A3, product stage)", BLUE)
group_box(3, 4, "Construction stage (A4-A5)", "#8a6d3b")

fig.suptitle("Figure 1. Ready-mix concrete production and construction process", fontsize=9.8,
             color=INK, y=0.99)
fig.tight_layout(rect=[0, 0, 1, 0.90])
fig.savefig(f"{OUT}/fig1_manufacturing_process.png", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# 2. EN 15804 life cycle stages (A1-D) declared-modules diagram
# ---------------------------------------------------------------------------
modules = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "B6", "B7",
           "C1", "C2", "C3", "C4", "D"]
group_labels = ["Product stage", "Construction\nstage", "Use stage", "End-of-life stage", "Benefits\n& loads"]
group_spans = [(0, 3), (3, 5), (5, 12), (12, 16), (16, 17)]

interbeton_declared = {m: True for m in modules}  # all declared
jsw_declared = {m: (m in ["A1", "A2", "A3", "A4", "C1", "C2", "C3", "C4", "D"]) for m in modules}

fig, ax = plt.subplots(figsize=(11, 3.6), dpi=200)
ax.set_xlim(-0.5, len(modules) - 0.5)
ax.set_ylim(0, 4)
ax.axis("off")

row_y = {"header": 3.15, "interbeton": 2.05, "jsw": 1.05}

# group headers spanning multiple module columns, aligned exactly to the
# left/right edges of the first and last module box in each group
for (start, end), label in zip(group_spans, group_labels):
    left = start - 0.4
    right = (end - 1) + 0.4
    width = right - left
    cx = (left + right) / 2
    box = FancyBboxPatch((left, row_y["header"] - 0.32), width, 0.64,
                          boxstyle="round,pad=0.0,rounding_size=0.05",
                          linewidth=1.0, edgecolor="#c3c2b7", facecolor="#f0efec")
    ax.add_patch(box)
    ax.text(cx, row_y["header"], label, ha="center", va="center", fontsize=8, color=INK)

# module letter row
for i, m in enumerate(modules):
    ax.text(i, row_y["header"] - 0.62, m, ha="center", va="center",
             fontsize=8.5, color=MUTED, fontweight="bold")

def draw_row(y, declared_map, color, row_label):
    ax.text(-1.05, y, row_label, ha="right", va="center", fontsize=9.2,
            color=INK, fontweight="bold")
    for i, m in enumerate(modules):
        declared = declared_map[m]
        face = color if declared else "#f4f3f0"
        edge = color if declared else "#d7d6d0"
        box = FancyBboxPatch((i - 0.4, y - 0.32), 0.8, 0.64,
                              boxstyle="round,pad=0.0,rounding_size=0.06",
                              linewidth=1.1, edgecolor=edge, facecolor=face, alpha=1.0)
        ax.add_patch(box)
        mark = "X" if declared else "MND"
        txt_color = "white" if declared else MUTED
        fs = 8.5 if declared else 6.6
        ax.text(i, y, mark, ha="center", va="center", fontsize=fs, color=txt_color,
                fontweight="bold")

draw_row(row_y["interbeton"], interbeton_declared, BLUE, "Interbeton\n(Greece)")
draw_row(row_y["jsw"], jsw_declared, GREEN, "JSW\n(India)")

legend_elems = [
    Line2D([0], [0], marker="s", color="none", markerfacecolor=BLUE, markersize=11, label="Interbeton, declared"),
    Line2D([0], [0], marker="s", color="none", markerfacecolor=GREEN, markersize=11, label="JSW, declared"),
    Line2D([0], [0], marker="s", color="none", markerfacecolor="#f4f3f0", markeredgecolor="#d7d6d0", markersize=11, label="Module Not Declared (MND)"),
]
ax.legend(handles=legend_elems, loc="lower center", bbox_to_anchor=(0.5, -0.06),
          ncol=3, frameon=False, fontsize=8.3)

fig.suptitle("Figure 2. EN 15804 life cycle modules (A1-D) declared by each EPD", fontsize=10, color=INK, y=1.03)
fig.tight_layout()
fig.savefig(f"{OUT}/fig2_lifecycle_modules.png", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# 3. LCA impact-category comparison charts (A1-A3), 2x2 small multiples
# ---------------------------------------------------------------------------
indicators = [
    ("Global Warming Potential (total)", "kg CO2 eq / m3", [154.5, 166.0]),
    ("Acidification Potential", "Mole H+ eq / m3", [0.3655, 0.605]),
    ("Eutrophication, freshwater", "kg P eq / m3", [0.01035, 0.0000487]),
    ("Water use (WDP)", "m3 world equiv. / m3", [99.2, 7.32]),
]
labels = ["Interbeton\nC12/15", "JSW\nM-20"]
colors = [BLUE, GREEN]

fig, axes = plt.subplots(2, 2, figsize=(7.6, 7.0), dpi=200)
for ax, (title, unit, values) in zip(axes.flat, indicators):
    bars = ax.bar(labels, values, color=colors, width=0.55, edgecolor="none")
    ax.set_title(title, fontsize=9.3, color=INK, pad=10)
    ax.set_ylabel(unit, fontsize=7.6, color=MUTED)
    ax.tick_params(axis="x", labelsize=8.4)
    ax.tick_params(axis="y", labelsize=7.2)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color("#c3c2b7")
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    ax.margins(y=0.15)
    for bar, v in zip(bars, values):
        fmt = f"{v:.4g}"
        ax.annotate(fmt, (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha="center", va="bottom", fontsize=8, color=INK,
                    xytext=(0, 3), textcoords="offset points")

fig.suptitle("Figure 3. Module A1-A3 (cradle to gate) impact comparison,\nthe only fully shared life cycle stage",
             fontsize=10.5, color=INK, y=1.01)
fig.tight_layout()
fig.savefig(f"{OUT}/fig3_lca_comparison.png", bbox_inches="tight")
plt.close(fig)


# ---------------------------------------------------------------------------
# Shared pie-chart builder: wedge leader-line labels (name + value), legend
# for the two colour categories placed below the plot so it never overlaps
# the pie itself.
# ---------------------------------------------------------------------------
def draw_market_cap_pie(companies, values, colors, value_fmt, title, out_name,
                          figsize=(9.0, 8.2)):
    fig, ax = plt.subplots(figsize=figsize, dpi=200)
    wedges, _ = ax.pie(values, colors=colors, startangle=90, counterclock=False,
                        radius=1.0,
                        wedgeprops=dict(edgecolor="white", linewidth=2))

    bbox_props = dict(boxstyle="round,pad=0.3", fc="#fcfcfb", ec="#c3c2b7", lw=0.8)

    # Wedge edge point (for the leader line start) and side (left/right),
    # keeping the wedge's own angle so lines fan out in the right direction.
    items = []
    for w, comp, val in zip(wedges, companies, values):
        ang_deg = (w.theta2 + w.theta1) / 2
        ang = np.deg2rad(ang_deg)
        x, y = np.cos(ang), np.sin(ang)
        side = 1 if x >= 0 else -1
        items.append(dict(comp=comp, val=val, x=x, y=y, ang_deg=ang_deg, side=side))

    label_x = 1.55  # fixed horizontal distance for every label, left/right
    y_top, y_bottom = 1.35, -1.35

    for side in (1, -1):
        side_items = [it for it in items if it["side"] == side]
        # keep the same top-to-bottom order the wedges appear in visually
        side_items.sort(key=lambda it: -it["y"])
        n = len(side_items)
        if n == 0:
            continue
        if n == 1:
            y_targets = [side_items[0]["y"]]
        else:
            y_targets = list(np.linspace(y_top, y_bottom, n))
        for it, y_t in zip(side_items, y_targets):
            it["y_target"] = y_t

    for it in items:
        ha = "left" if it["side"] >= 0 else "right"
        conn_style = f"angle,angleA=0,angleB={it['ang_deg']:.0f}"
        ax.annotate(f"{it['comp']}\n{value_fmt(it['val'])}",
                     xy=(it["x"] * 1.0, it["y"] * 1.0),
                     xytext=(label_x * it["side"], it["y_target"]),
                     ha=ha, va="center", fontsize=8.6, bbox=bbox_props,
                     arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.0,
                                     connectionstyle=conn_style),
                     zorder=3)

    ax.set_title(title, fontsize=11.2, color=INK, pad=18)

    legend_elems = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=ORANGE, markersize=12,
               label="Company profiled in this assignment"),
        Line2D([0], [0], marker="s", color="none", markerfacecolor=GRAY, markersize=12,
               label="Other competitor"),
    ]
    ax.legend(handles=legend_elems, loc="upper center", bbox_to_anchor=(0.5, -0.04),
              ncol=1, frameon=False, fontsize=9.5)
    ax.set_xlim(-2.35, 2.35)
    ax.set_ylim(-1.75, 1.75)
    fig.tight_layout()
    fig.savefig(f"{OUT}/{out_name}", bbox_inches="tight")
    plt.close(fig)


# 4a. Global cement/concrete majors, market cap
global_companies = ["CRH", "Holcim", "UltraTech Cement", "Heidelberg Materials",
                    "Anhui Conch", "TITAN Cement\nInternational", "JSW Cement"]
global_capm_usd_bn = [69.29, 52.75, 40.30, 35.26, 18.22, 4.34, 1.96]
global_colors = [GRAY, GRAY, GRAY, GRAY, GRAY, ORANGE, ORANGE]

draw_market_cap_pie(
    global_companies, global_capm_usd_bn, global_colors,
    value_fmt=lambda v: f"${v:.2f}B",
    title="Figure 4. Global cement/concrete majors by market capitalization,\nwith the two companies in this study highlighted",
    out_name="fig4_global_market_cap.png",
)

# 4b. India cement peers, market cap
india_companies = ["UltraTech Cement", "Shree Cement", "Ambuja Cements", "ACC",
                    "Dalmia Bharat", "JSW Cement"]
india_capm_cr = [330773.51, 125979, 108736, 95538, 49737, 18844]
india_colors = [GRAY, GRAY, GRAY, GRAY, GRAY, ORANGE]

draw_market_cap_pie(
    india_companies, india_capm_cr, india_colors,
    value_fmt=lambda v: f"Rs.{v:,.0f} Cr",
    title="Figure 5. India's ready-mix/cement peer group by market capitalization,\nwith JSW Cement highlighted",
    out_name="fig5_india_market_cap.png",
)

print("done")
