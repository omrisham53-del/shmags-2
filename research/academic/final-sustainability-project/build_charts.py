# -*- coding: utf-8 -*-
"""
Charts for the Final Sustainability Project (Herzliya marina stormwater).

Every number here comes from a cited source. Nothing is interpolated or invented.
  - Beach water quality figures: מבקר עיריית הרצליה (2021), sections 9.2-9.3
  - Removal efficiencies: Drapper & Hornbuckle (2018)
  - Outlet compliance matrix: מבקר עיריית הרצליה (2021), section 5.2
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from bidi.algorithm import get_display

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["font.family"] = "Segoe UI"
plt.rcParams["axes.unicode_minus"] = False

# palette
NAVY = "#123B5C"
TEAL = "#2E8B9A"
CORAL = "#D45B4E"
SAND = "#E8DCC8"
GREY = "#8A9299"
INK = "#1E2A32"


def he(s):
    """Hebrew strings must be bidi-reordered; matplotlib lays text out LTR."""
    return get_display(s)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


# ---------------------------------------------------------------- chart 01
def chart_bathing_season():
    """Herzliya bathing-season exceedance rate, 2019 vs 2020. Auditor s.9.3."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    years = ["2019", "2020"]
    vals = [3.0, 6.8]
    bars = ax.bar(years, vals, color=[GREY, CORAL], width=0.5,
                  edgecolor=INK, linewidth=0.8)

    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.18, f"{v}%",
                ha="center", va="bottom", fontsize=13, fontweight="bold", color=INK)

    ax.annotate("", xy=(1, 6.8), xytext=(0, 3.0),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.6,
                                connectionstyle="arc3,rad=-0.35"))
    ax.text(0.5, 5.6, he("גידול של 126%"), ha="center", fontsize=12,
            color=CORAL, fontweight="bold")

    ax.set_ylabel(he("שיעור דגימות חורגות (%)"), fontsize=11)
    ax.set_title(he("שיעור הדגימות החורגות בחופי הרצליה, עונת הרחצה"),
                 fontsize=13, fontweight="bold", pad=14)
    ax.set_ylim(0, 8.4)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.25, linestyle=":")
    ax.set_axisbelow(True)
    fig.text(0.5, -0.04, he("מקור: מבקר עיריית הרצליה (2021), סעיף 9.3"),
             ha="center", fontsize=8.5, color=GREY)
    save(fig, "01_bathing_season_exceedance.png")


# ---------------------------------------------------------------- chart 02
def chart_removal():
    """Media filter removal efficiency. Drapper & Hornbuckle (2018)."""
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    labels = [he("מוצקים מרחפים"), he("זרחן"), he("מתכות כבדות")]
    vals = [80, 60, 50]
    colors = [TEAL, NAVY, "#4A7C8C"]

    bars = ax.barh(labels, vals, color=colors, height=0.55,
                   edgecolor=INK, linewidth=0.8)
    for b, v in zip(bars, vals):
        ax.text(v + 1.5, b.get_y() + b.get_height() / 2, f"{v}%",
                va="center", fontsize=12, fontweight="bold", color=INK)

    ax.set_xlim(0, 100)
    ax.set_xlabel(he("שיעור הרחקה (%)"), fontsize=11)
    ax.set_title(he("יעילות הרחקת מזהמים במערכת מדיה פילטר, ניטור שדה 4 שנים"),
                 fontsize=12.5, fontweight="bold", pad=14)
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", alpha=0.25, linestyle=":")
    ax.set_axisbelow(True)
    fig.text(0.5, -0.04,
             he("מקור: Drapper & Hornbuckle (2018), דרום מזרח קווינסלנד"),
             ha="center", fontsize=8.5, color=GREY)
    save(fig, "02_removal_efficiency.png")


# ---------------------------------------------------------------- chart 03
def chart_outlet_matrix():
    """Compliance matrix across the 4 outlets. Auditor s.5.2."""
    outlets = ["מרינה צפון", "מרינה דרום", "מוצא איינשטיין", "מלון השרון"]
    measures = ["פתרון למי קיץ", "שיכוך אנרגיית זרימה", "אמצעי ללכידת פסולת"]
    # 2 = exists, 1 = partial / non-conforming, 0 = absent
    data = [
        [2, 2, 0],   # מרינה צפון
        [0, 2, 0],   # מרינה דרום
        [0, 1, 0],   # מוצא איינשטיין
        [0, 0, 0],   # מלון השרון
    ]
    cmap = {2: TEAL, 1: "#E0A33E", 0: "#D9DDE0"}
    txt = {2: "קיים", 1: "חלקי", 0: "אינו קיים"}

    fig, ax = plt.subplots(figsize=(8.2, 3.9))
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            ax.add_patch(FancyBboxPatch(
                (c, -r), 0.92, 0.82,
                boxstyle="round,pad=0.012,rounding_size=0.05",
                facecolor=cmap[v], edgecolor="white", linewidth=2))
            ax.text(c + 0.46, -r + 0.41, he(txt[v]), ha="center", va="center",
                    fontsize=10.5, color="white" if v != 0 else GREY,
                    fontweight="bold" if v != 0 else "normal")

    ax.set_xlim(-0.05, 3.0)
    ax.set_ylim(-3.25, 1.15)
    ax.set_xticks([c + 0.46 for c in range(3)])
    ax.set_xticklabels([he(m) for m in measures], fontsize=10.5)
    ax.xaxis.tick_top()
    ax.set_yticks([-r + 0.41 for r in range(4)])
    ax.set_yticklabels([he(o) for o in outlets], fontsize=10.5)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(he("מצב האמצעים בארבעת מוצאי הניקוז אל הים"),
                 fontsize=12.5, fontweight="bold", pad=34)
    fig.text(0.5, -0.02, he("מקור: מבקר עיריית הרצליה (2021), סעיף 5.2"),
             ha="center", fontsize=8.5, color=GREY)
    save(fig, "03_outlet_matrix.png")


# ---------------------------------------------------------------- chart 04
def chart_treatment_train():
    """Schematic of the proposed treatment train. No data, design only."""
    fig, ax = plt.subplots(figsize=(9.2, 2.9))
    stages = [
        ("1", "איסוף ולכידה", "סל/סורג לפסולת גסה", SAND, INK),
        ("2", "השקעה", "תא שיקוע לחלקיקים", "#BFD4C8", INK),
        ("3", "סינון וטיהור", "מדיה פילטר / ביופילטר", TEAL, "white"),
        ("4", "יציאה לים", "מים מטופלים", NAVY, "white"),
    ]
    w, gap = 1.85, 0.42
    for i, (num, title, sub, fc, tc) in enumerate(stages):
        x = i * (w + gap)
        ax.add_patch(FancyBboxPatch(
            (x, 0), w, 1.28,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=fc, edgecolor=INK, linewidth=1.1))
        ax.text(x + w / 2, 0.92, num, ha="center", va="center",
                fontsize=15, fontweight="bold", color=tc, alpha=0.55)
        ax.text(x + w / 2, 0.60, he(title), ha="center", va="center",
                fontsize=11.5, fontweight="bold", color=tc)
        ax.text(x + w / 2, 0.28, he(sub), ha="center", va="center",
                fontsize=9, color=tc)
        if i < len(stages) - 1:
            ax.add_patch(FancyArrowPatch(
                (x + w + 0.06, 0.64), (x + w + gap - 0.06, 0.64),
                arrowstyle="-|>", mutation_scale=17, color=INK, lw=1.6))

    # flow direction note (RTL reading, so mark left end as the sea)
    ax.set_xlim(-0.25, 4 * w + 3 * gap + 0.25)
    ax.set_ylim(-0.42, 1.62)
    ax.axis("off")
    ax.set_title(he("רכבת הטיפול המוצעת במוצא הניקוז"),
                 fontsize=12.5, fontweight="bold", pad=10)
    save(fig, "04_treatment_train.png")


if __name__ == "__main__":
    chart_bathing_season()
    chart_removal()
    chart_outlet_matrix()
    chart_treatment_train()
    print("done")
