import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUT = r"C:\עמרי\Shmags 2\research\academic\hw3-lca-cups\HW3_LCA_Cups.pdf"
LOGO_PATH = r"C:\עמרי\Shmags 2\references\brand-assets\university-logos\reichman-main-logo.png"
COURSE_NAME = "Circular Economy, Industrial Ecology, and Life Cycle Assessment (LCA)"

NAVY  = colors.HexColor("#0D1B2A")
TEAL  = colors.HexColor("#1ABC9C")
BLUE  = colors.HexColor("#1A73E8")
LGRAY = colors.HexColor("#F4F6F9")
MGRAY = colors.HexColor("#D0D7E2")
WHITE = colors.white
BLACK = colors.black
GREEN = colors.HexColor("#27AE60")
RED   = colors.HexColor("#E74C3C")

base = getSampleStyleSheet()

def S(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

styles = {
    "cover_title": S("cover_title", "Title",
        fontSize=26, textColor=NAVY, leading=32, spaceAfter=8, alignment=TA_CENTER),
    "cover_sub": S("cover_sub", "Normal",
        fontSize=12, textColor=TEAL, leading=18, alignment=TA_CENTER),
    "cover_meta": S("cover_meta", "Normal",
        fontSize=10, textColor=colors.HexColor("#7F8C8D"), leading=15, alignment=TA_CENTER),
    "h1": S("h1", "Heading1",
        fontSize=15, textColor=NAVY, leading=20, spaceBefore=16, spaceAfter=5),
    "h2": S("h2", "Heading2",
        fontSize=11, textColor=BLUE, leading=15, spaceBefore=12, spaceAfter=3),
    "body": S("body", "Normal",
        fontSize=9.5, leading=14, spaceAfter=4, alignment=TA_JUSTIFY),
    "bullet": S("bullet", "Normal",
        fontSize=9.5, leading=13, leftIndent=14, bulletIndent=4, spaceAfter=2),
    "label": S("label", "Normal",
        fontSize=8, textColor=colors.HexColor("#7F8C8D"), leading=11),
    "small": S("small", "Normal",
        fontSize=8, leading=11, spaceAfter=2),
}

def H1(text):
    return [
        Spacer(1, 0.15*cm),
        Paragraph(text, styles["h1"]),
    ]

def H2(text): return [Paragraph(text, styles["h2"])]
def P(text):  return [Paragraph(text, styles["body"])]
def SP(n=0.3): return [Spacer(1, n*cm)]

def _wrap(cell, hdr_style, cell_style, is_hdr):
    if isinstance(cell, str):
        return Paragraph(cell, hdr_style if is_hdr else cell_style)
    return cell

def tbl(data, col_widths, header_row=True, font_size=8.5):
    """Table with all string cells wrapped in Paragraph for proper word wrapping."""
    cell_s = ParagraphStyle("_tc", parent=base["Normal"],
        fontSize=font_size, leading=font_size * 1.35)
    hdr_s = ParagraphStyle("_th", parent=base["Normal"],
        fontSize=font_size, leading=font_size * 1.35,
        textColor=WHITE, fontName="Helvetica-Bold")
    wrapped = [
        [_wrap(c, hdr_s, cell_s, header_row and r == 0) for c in row]
        for r, row in enumerate(data)
    ]
    t = Table(wrapped, colWidths=col_widths, repeatRows=1 if header_row else 0)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0 if header_row else -1), NAVY if header_row else LGRAY),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [WHITE, LGRAY]),
        ("GRID",          (0, 0), (-1, -1), 0.4, MGRAY),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    return t

def result_box(label, value, unit, color, pct_label=None):
    cell_s = ParagraphStyle("rb", parent=base["Normal"],
        fontSize=9, textColor=WHITE, leading=13, alignment=TA_CENTER)
    val_s  = ParagraphStyle("rv", parent=base["Normal"],
        fontSize=20, textColor=WHITE, fontName="Helvetica-Bold",
        leading=24, alignment=TA_CENTER)
    sub_s  = ParagraphStyle("rs", parent=base["Normal"],
        fontSize=8, textColor=MGRAY, leading=11, alignment=TA_CENTER)
    rows = [
        [Paragraph(label, cell_s)],
        [Paragraph(f"{value} {unit}", val_s)],
    ]
    if pct_label:
        rows.append([Paragraph(pct_label, sub_s)])
    t = Table(rows, colWidths=[7.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), color),
        ("LEFTPADDING",   (0,0),(-1,-1), 10),
        ("RIGHTPADDING",  (0,0),(-1,-1), 10),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("ROWBACKGROUNDS",(0,0),(-1,-1), [color]),
        ("BOX",           (0,0),(-1,-1), 0, color),
    ]))
    return t

# Page templates
def cover_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(TEAL)
    canvas.rect(0, h - 1.0*cm, w, 1.0*cm, fill=1, stroke=0)
    canvas.rect(0, 0, w, 0.5*cm, fill=1, stroke=0)
    canvas.restoreState()

def normal_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(TEAL)
    canvas.rect(0, h - 0.5*cm, w, 0.5*cm, fill=1, stroke=0)
    canvas.setFillColor(MGRAY)
    canvas.rect(0, 0, w, 0.5*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor("#7F8C8D"))
    canvas.drawCentredString(w/2, 0.17*cm,
        "HW Assignment #3 - LCA Exercise | Option B: Single-Use vs. Reusable Cup | Omri Shamgar, Tom Ginel, Tomer Tasa | June 2026")
    canvas.restoreState()

def on_page(canvas, doc):
    if doc.page == 1:
        cover_page(canvas, doc)
    else:
        normal_page(canvas, doc)

# Document
doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=1.5*cm,
    title="HW3 LCA Exercise - Option B",
    author="Omri Shamgar",
)

story = []

# COVER
story += [Spacer(1, 2.5*cm)]

if os.path.exists(LOGO_PATH):
    logo = Image(LOGO_PATH, width=5*cm, height=2*cm, hAlign="CENTER")
    story += [logo, Spacer(1, 0.8*cm)]
else:
    story += [Spacer(1, 1.5*cm)]

story += [Paragraph("HW ASSIGNMENT #3", styles["cover_title"])]
story += [Paragraph("LCA Exercise", ParagraphStyle(
    "ct2", parent=base["Normal"], fontSize=20, textColor=TEAL,
    alignment=TA_CENTER, spaceAfter=10))]
story += [Spacer(1, 0.4*cm)]
story += [HRFlowable(width="60%", thickness=1, color=TEAL, hAlign="CENTER", spaceAfter=14)]
story += [Paragraph(
    "Option B: Single-Use Cup vs. Reusable Steel Cup<br/>at the Karnaf Store, Reichman University",
    styles["cover_sub"])]
story += [Spacer(1, 2*cm)]
story += [Paragraph("Omri Shamgar &nbsp;|&nbsp; Tom Ginel &nbsp;|&nbsp; Tomer Tasa", styles["cover_meta"])]
story += [Paragraph(
    f"{COURSE_NAME} &nbsp;|&nbsp; Reichman University &nbsp;|&nbsp; June 2026",
    styles["cover_meta"])]
story += [PageBreak()]

# Q1: FUNCTIONAL UNIT
story += H1("1. Functional Unit")
story += P(
    "The functional unit is: <b>serving one hot drink per day over 20 consecutive days "
    "at the Karnaf store, Reichman University</b> (20 servings total)."
)
story += P(
    "This unit allows direct comparison between the two systems: 20 single-use paper cups with "
    "polystyrene (PS) lids (Product A) versus one reusable stainless steel cup with silicone lid "
    "and silicone heat-resistant wrapper, used 20 times (Product B)."
)
story += SP(0.2)

# Q2: SYSTEM BOUNDARIES TYPE
story += H1("2. System Boundaries Type")
story += P(
    "Both products are assessed using a <b>cradle-to-grave</b> system boundary approach, "
    "with the following stage coverage per product:"
)
story += [tbl(
    [["", "Product A - Single-Use Cup", "Product B - Reusable Steel Cup"],
     ["Raw material production", "Included", "Included"],
     ["Transport to production site", "Included", "Included"],
     ["Manufacturing", "Included", "Included"],
     ["Transport to Reichman University", "Excluded (not in assignment scope)", "Included (explicitly stated)"],
     ["Use phase (washing)", "Not applicable", "Included (20 washes)"],
     ["End-of-life / disposal", "Included (incineration after each use)", "Excluded (per assignment scope)"],
     ["Coffee production / store operations", "Excluded", "Excluded"]],
    [3.5*cm, 6.5*cm, 6.5*cm]
)]
story += SP(0.2)
story += P(
    "The main structural asymmetry is that Product A includes disposal (cups are discarded after each use) "
    "while Product B excludes end-of-life per the assignment instructions. This is noted as a limitation "
    "when comparing the two totals on a fully equivalent basis."
)
story += SP(0.2)

# Q3: SYSTEM BOUNDARY DIAGRAM
story += H1("3. System Boundary Diagrams")

story += H2("Product A - Single-Use Paper Cup (20 cups)")
flow_a = [
    ["STAGE", "ACTIVITY", "IN / OUT OF SCOPE"],
    ["Raw materials", "Paper (Hedera) | LDPE (Haifa) | PS (Haifa)", "IN"],
    ["Transport", "Lorry to production site in Natanya (~38-63 km)", "IN"],
    ["Manufacturing", "Cup forming (0.04 kWh/cup, IL grid) | LDPE coating application", "IN"],
    ["Transport to RU", "Natanya to Herzliya (~30 km)", "OUT (not in scope)"],
    ["Use", "20 cups used, 1 per day over 20 days", "IN (defines scale)"],
    ["End-of-life", "Municipal incineration after each use (paper + LDPE + PS)", "IN"],
    ["Excluded", "Coffee, filling, water, store operations, ink", "OUT"],
]
story += [tbl(flow_a, [3.0*cm, 8.5*cm, 5.0*cm])]
story += SP(0.3)

story += H2("Product B - Reusable Steel Cup (1 cup, 20 uses)")
flow_b = [
    ["STAGE", "ACTIVITY", "IN / OUT OF SCOPE"],
    ["Raw materials", "Steel 18/8 (Espoo) | Silicone lid (Espoo) | Silicone wrapper (Espoo)", "IN"],
    ["Transport (FI)", "Lorry: Espoo to Helsinki (~20 km)", "IN"],
    ["Manufacturing", "Cold impact extrusion (steel) | Silicone shaping (0.4 kWh/kg, FI grid)", "IN"],
    ["Transport to RU", "Container ship: Helsinki to Herzliya (~7,500 km)", "IN"],
    ["Use phase", "20 washes: 0.7 L water + 5 g soap per wash", "IN"],
    ["End-of-life", "Not assessed (excluded per assignment)", "OUT"],
    ["Excluded", "Coffee, store operations, transport store to user", "OUT"],
]
story += [tbl(flow_b, [3.0*cm, 8.5*cm, 5.0*cm])]
story += SP(0.2)

story += [PageBreak()]

# Q4: ASSUMPTIONS
story += H1("4. Main Assumptions")

ah = ParagraphStyle("ah", parent=base["Normal"], fontSize=9, fontName="Helvetica-Bold", leading=13)
ad = ParagraphStyle("ad", parent=base["Normal"], fontSize=9, leading=13)

assumptions = [
    ("<b>Transport distances (estimated):</b>",
     "Hedera to Natanya: ~38 km; Haifa to Natanya: ~63 km; "
     "Espoo to Helsinki: ~20 km; Helsinki to Herzliya by sea: ~7,500 km "
     "(via Baltic Sea, North Sea, English Channel, Strait of Gibraltar, Mediterranean)."),
    ("<b>Lorry dataset - Israel proxy:</b>",
     "No Israel-specific lorry transport dataset exists in the BAFU database. "
     "The European average (RER) fleet average for 16t-32t lorries is used as a proxy. "
     "This is standard LCA practice when the exact country is unavailable."),
    ("<b>Paper material:</b>",
     "Kraft paper, unbleached {RER} was selected as the closest available proxy for the paper cup body. "
     "No dedicated food-service paperboard or paper cup dataset exists in the BAFU 2025 database."),
    ("<b>Polystyrene grade:</b>",
     "General Purpose Polystyrene (GPPS) {RER} was selected for the injection-molded PS lid, "
     "as GPPS is the standard grade used for rigid food packaging lids."),
    ("<b>Steel grade:</b>",
     "Chromium steel 18/8 {RER} (i.e., 304 stainless steel) was selected for the reusable cup body. "
     "This is the industry-standard grade for reusable drinkware. The RER geography is used as a proxy "
     "for Finnish production; no FI-specific stainless steel dataset exists in BAFU."),
    ("<b>Finland electricity:</b>",
     "The Electricity, production mix {FI} dataset (0.102 kgCO2eq/kWh) was used, representing the "
     "national grid average. Finland's grid is predominantly nuclear and hydropower, which explains the low factor."),
    ("<b>Tap water - Israel proxy:</b>",
     "The RER (European average) tap water dataset was used as no Israel-specific dataset exists. "
     "Israel relies heavily on desalinated water (~9.68x10<super>-3</super> kgCO2eq/kg) vs RER "
     "(2.03x10<super>-4</super> kgCO2eq/kg). Given water's small share of total GWP, "
     "this underestimation is negligible."),
    ("<b>LDPE coating emission:</b>",
     "The process emission of 0.002 kgCO2eq/cup was provided directly in the assignment and applied "
     "as a direct emission, not linked to a BAFU dataset."),
    ("<b>Disposal (Product A):</b>",
     "All 20 cups and lids are sent to municipal incineration. Coated paper cups cannot enter standard "
     "paper recycling streams due to the plastic lining, making incineration the appropriate end-of-life route."),
    ("<b>No processing losses (Product A):</b>",
     "The assignment explicitly states no waste is generated during cup production."),
    ("<b>Cold impact extrusion (Product B):</b>",
     "The BAFU dataset 'Deformation stroke, cold impact extrusion, steel {RER}' "
     "(3.36x10<super>-2</super> kgCO2eq/kg) was applied per kg of steel formed. "
     "This covers forming energy only; steel raw material is accounted for separately."),
    ("<b>Transport Natanya to RU (Product A):</b>",
     "Excluded from scope, as the assignment defines Product A's transport only as materials "
     "to production site. The impact of including it would be ~0.002 kgCO2eq (0.2% of total A), "
     "which is negligible."),
]

for header, detail in assumptions:
    row = [[Paragraph(header, ah), Paragraph(detail, ad)]]
    t = Table(row, colWidths=[4.0*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(0,0), LGRAY),
        ("BACKGROUND",   (1,0),(1,0), WHITE),
        ("BOX",          (0,0),(-1,-1), 0.4, MGRAY),
        ("INNERGRID",    (0,0),(-1,-1), 0.3, MGRAY),
        ("LEFTPADDING",  (0,0),(-1,-1), 6),
        ("RIGHTPADDING", (0,0),(-1,-1), 6),
        ("TOPPADDING",   (0,0),(-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ]))
    story += [t, Spacer(1, 0.12*cm)]

story += [PageBreak()]

# Q5: GWP RESULTS
story += H1("5. Total GWP Results")

story += H2("Product A - Single-Use Cup (20 cups, 20 lids)")
story += [tbl(
    [["Life Cycle Stage", "GWP [kgCO2eq]", "Contribution [%]", "Notes"],
     ["Raw materials", "0.510", "42.6%", "Paper + LDPE + Polystyrene (PS dominates)"],
     ["Transport (to production site)", "0.003", "0.3%", "Short intra-Israel distances"],
     ["Processing", "0.358", "29.9%", "Cup forming electricity + LDPE coating"],
     ["Disposal (incineration)", "0.327", "27.3%", "Paper + LDPE + PS after each use"],
     ["TOTAL", "1.197", "100%", ""]],
    [5.5*cm, 3.5*cm, 3.0*cm, 4.5*cm]
)]
story += SP(0.3)

story += H2("Product B - Reusable Steel Cup (1 cup, 20 uses)")
story += [tbl(
    [["Life Cycle Stage", "GWP [kgCO2eq]", "Contribution [%]", "Notes"],
     ["Raw materials", "0.775", "79.6%", "Steel dominates; silicone secondary"],
     ["Transport", "0.024", "2.4%", "Sea freight Helsinki to Herzliya"],
     ["Processing (manufacturing)", "0.007", "0.7%", "Low due to Finland's clean grid"],
     ["Use phase (20 washes)", "0.169", "17.3%", "Soap contributes 17.0%; water negligible"],
     ["TOTAL", "0.974", "100%", "End-of-life excluded per assignment"]],
    [5.5*cm, 3.5*cm, 3.0*cm, 4.5*cm]
)]
story += SP(0.4)

# Result boxes side by side
box_a = result_box("Product A - 20 Single-Use Cups", "1.197", "kgCO2eq",
                   colors.HexColor("#C0392B"), "Higher GWP")
box_b = result_box("Product B - Reusable Cup (20 uses)", "0.974", "kgCO2eq",
                   GREEN, "Lower GWP (-19%)")
comp = Table([[box_a, Spacer(1.5*cm, 0.1*cm), box_b]], colWidths=[7.5*cm, 1.5*cm, 7.5*cm])
comp.setStyle(TableStyle([
    ("LEFTPADDING",  (0,0),(-1,-1), 0),
    ("RIGHTPADDING", (0,0),(-1,-1), 0),
    ("TOPPADDING",   (0,0),(-1,-1), 0),
    ("BOTTOMPADDING",(0,0),(-1,-1), 0),
    ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
]))
story += [comp]
story += SP(0.3)
story += P(
    "The reusable cup has approximately <b>19% lower GWP</b> over the 20-day comparison period. "
    "Importantly, Product B's manufacturing emissions are fixed regardless of how many times the cup "
    "is used. With additional uses, the gap widens further in favor of the reusable option."
)
story += SP(0.2)

# Q6: BIGGEST CONTRIBUTOR
story += H1("6. Largest GWP Contributor")

story += H2("Product A - Polystyrene (PS)")
story += P(
    "The largest single contributor is <b>polystyrene (PS)</b>. Its raw material production "
    "contributes 0.292 kgCO2eq (24.4% of total), and its incineration at end-of-life adds "
    "another 0.256 kgCO2eq (21.4%). Combined, the PS lid accounts for <b>45.8%</b> of "
    "Product A's total GWP - nearly half the entire footprint of 20 disposable cups. "
    "Cup-forming electricity is the next largest single item at 26.5%, reflecting Israel's "
    "relatively carbon-intensive grid (0.397 kgCO2eq/kWh)."
)
story += [tbl(
    [["Flow", "GWP [kgCO2eq]", "% of Total A"],
     ["PS raw material production", "0.292", "24.4%"],
     ["Cup forming electricity", "0.318", "26.5%"],
     ["PS incineration (disposal)", "0.256", "21.4%"],
     ["Paper raw material", "0.171", "14.3%"],
     ["LDPE disposal", "0.061", "5.1%"],
     ["LDPE coating process", "0.040", "3.3%"],
     ["LDPE raw material", "0.047", "3.9%"],
     ["Transport", "0.003", "0.3%"],
     ["Paper disposal", "0.010", "0.9%"]],
    [8*cm, 4*cm, 4.5*cm]
)]
story += SP(0.3)

story += H2("Product B - Stainless Steel (18/8)")
story += P(
    "Steel production dominates at <b>68.1%</b> of total GWP (0.663 out of 0.974 kgCO2eq). "
    "This reflects the energy-intensive nature of stainless steel manufacturing. "
    "Soap consumption over 20 washes is the second-largest contributor at 17.0% - "
    "notable given that only 100 g of soap is used in total. This underscores that the "
    "use-phase cleaning routine, rather than manufacturing, drives the ongoing emissions of "
    "the reusable product."
)
story += [tbl(
    [["Flow", "GWP [kgCO2eq]", "% of Total B"],
     ["Steel production (18/8)", "0.663", "68.1%"],
     ["Soap (20 washes)", "0.166", "17.0%"],
     ["Silicone lid production", "0.070", "7.2%"],
     ["Silicone wrapper production", "0.042", "4.3%"],
     ["Sea transport (Helsinki to Herzliya)", "0.023", "2.3%"],
     ["Water (20 washes)", "0.003", "0.3%"],
     ["Cold impact extrusion", "0.005", "0.5%"],
     ["Processing (FI electricity)", "0.002", "0.2%"],
     ["Land transport (Espoo to Helsinki)", "0.001", "0.1%"]],
    [8*cm, 4*cm, 4.5*cm]
)]

story += [PageBreak()]

# APPENDIX
story += H1("Appendix - Inventory Table: Product A (Single-Use Cup)")

# Col widths: material(2.8) qty(1.0) unit(0.7) dataset(3.2) geo(0.8) EF(1.9) GWP(1.6) %(1.1) notes(3.4) = 16.5cm
ACOLS = [2.8*cm, 1.0*cm, 0.7*cm, 3.2*cm, 0.8*cm, 1.9*cm, 1.6*cm, 1.1*cm, 3.4*cm]

def app_tbl(data):
    """Appendix table with Paragraph wrapping in all cells."""
    cell_s = ParagraphStyle("_atc", parent=base["Normal"], fontSize=7.0, leading=10)
    hdr_s = ParagraphStyle("_ath", parent=base["Normal"],
        fontSize=7.0, leading=10, textColor=WHITE, fontName="Helvetica-Bold")
    wrapped = [
        [_wrap(c, hdr_s, cell_s, r == 0) for c in row]
        for r, row in enumerate(data)
    ]
    t = Table(wrapped, colWidths=ACOLS, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,0), NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LGRAY]),
        ("GRID",          (0,0),(-1,-1), 0.3, MGRAY),
        ("LEFTPADDING",   (0,0),(-1,-1), 3),
        ("RIGHTPADDING",  (0,0),(-1,-1), 3),
        ("TOPPADDING",    (0,0),(-1,-1), 3),
        ("BOTTOMPADDING", (0,0),(-1,-1), 3),
        ("VALIGN",        (0,0),(-1,-1), "TOP"),
    ]))
    return t

HDR = ["Material / flow / activity", "Qty", "Unit", "BAFU Dataset",
       "Geo", "EF [kgCO2eq/unit]", "GWP [kgCO2eq]", "%", "Notes / assumptions"]

data_a = [
    HDR,
    ["Paper (cup body)", "0.240", "kg",
     "Kraft paper, unbleached, at plant", "RER",
     "7.11E-01", "0.1707", "14.3%",
     "20 cups x 0.012 kg. No paper-cup dataset in BAFU; unbleached kraft used as proxy."],
    ["LDPE (coating)", "0.020", "kg",
     "Polyethylene, LDPE, granulate, at plant", "RER",
     "2.35E+00", "0.0470", "3.9%",
     "20 cups x 0.001 kg."],
    ["Polystyrene (lid)", "0.080", "kg",
     "Polystyrene, general purpose, GPPS, at plant", "RER",
     "3.65E+00", "0.2920", "24.4%",
     "20 lids x 0.004 kg. GPPS selected for rigid injection-molded lid."],
    ["Transport - Paper (Hedera to Natanya)", "0.00912", "tkm",
     "Transport, freight, lorry, 16t-32t gross weight, fleet average", "RER",
     "2.22E-01", "0.0020", "0.2%",
     "0.240 kg x 38 km. RER proxy for Israel; no IL-specific dataset."],
    ["Transport - LDPE (Haifa to Natanya)", "0.00126", "tkm",
     "Transport, freight, lorry, 16t-32t gross weight, fleet average", "RER",
     "2.22E-01", "0.0003", "0.0%",
     "0.020 kg x 63 km."],
    ["Transport - PS (Haifa to Natanya)", "0.00504", "tkm",
     "Transport, freight, lorry, 16t-32t gross weight, fleet average", "RER",
     "2.22E-01", "0.0011", "0.1%",
     "0.080 kg x 63 km."],
    ["Cup forming (Israel electricity)", "0.800", "kWh",
     "Given in assignment (IL grid)", "IL",
     "3.97E-01", "0.3176", "26.5%",
     "20 cups x 0.04 kWh. Israel grid emission factor given directly."],
    ["LDPE coating process", "20", "cups",
     "Given in assignment (direct emission)", "IL",
     "2.00E-03/cup", "0.0400", "3.3%",
     "Direct process emission as specified in assignment."],
    ["Disposal - Paper (incineration)", "0.240", "kg",
     "Disposal, packaging paper, 13.7% water, to municipal incineration", "CH",
     "4.33E-02", "0.0104", "0.9%",
     "Coated paper cannot be recycled; incineration assumed. CH proxy for IL."],
    ["Disposal - LDPE (incineration)", "0.020", "kg",
     "Disposal, polyethylene, 0.4% water, to municipal incineration", "CH",
     "3.03E+00", "0.0606", "5.1%",
     "LDPE coating disposed with cup body. CH proxy for IL."],
    ["Disposal - PS (incineration)", "0.080", "kg",
     "Disposal, polystyrene, 0.2% water, to municipal incineration", "CH",
     "3.20E+00", "0.2560", "21.4%",
     "20 PS lids after use. CH proxy for IL."],
    ["TOTAL", "", "", "", "", "", "1.197", "100%", ""],
]

story += [app_tbl(data_a)]
story += SP(0.4)

story += H1("Appendix - Inventory Table: Product B (Reusable Steel Cup)")

data_b = [
    HDR,
    ["Steel (cup body)", "0.150", "kg",
     "Chromium steel 18/8, at plant", "RER",
     "4.42E+00", "0.6630", "68.1%",
     "304 stainless steel (18/8). RER used; no FI-specific stainless steel dataset in BAFU."],
    ["Silicone (lid)", "0.025", "kg",
     "Silicone product, at plant", "RER",
     "2.79E+00", "0.0698", "7.2%",
     ""],
    ["Silicone (wrapper)", "0.015", "kg",
     "Silicone product, at plant", "RER",
     "2.79E+00", "0.0419", "4.3%",
     ""],
    ["Transport - land (Espoo to Helsinki)", "0.00380", "tkm",
     "Transport, freight, lorry, 16t-32t gross weight, fleet average", "RER",
     "2.22E-01", "0.0008", "0.1%",
     "0.190 kg total x 20 km."],
    ["Transport - sea (Helsinki to Herzliya)", "1.4250", "tkm",
     "Transport, transoceanic container ship", "OCE",
     "1.60E-02", "0.0228", "2.3%",
     "0.190 kg x 7,500 km. Route via North Sea, English Channel, Mediterranean."],
    ["Silicone lid shaping (Finland electricity)", "0.0100", "kWh",
     "Electricity, production mix", "FI",
     "1.02E-01", "0.0010", "0.1%",
     "0.4 kWh/kg x 0.025 kg."],
    ["Silicone wrapper shaping (Finland electricity)", "0.0060", "kWh",
     "Electricity, production mix", "FI",
     "1.02E-01", "0.0006", "0.1%",
     "0.4 kWh/kg x 0.015 kg."],
    ["Cold impact extrusion (steel cup)", "0.150", "kg",
     "Deformation stroke, cold impact extrusion, steel", "RER",
     "3.36E-02", "0.0050", "0.5%",
     "Forming process only; steel material accounted separately above."],
    ["Tap water (20 washes)", "14.00", "kg",
     "Tap water, at user", "RER",
     "2.03E-04", "0.0028", "0.3%",
     "14 L total (0.7 L x 20). RER proxy; IL uses desalination (slightly higher factor, negligible impact)."],
    ["Soap (20 washes)", "0.100", "kg",
     "Soap, at plant", "RER",
     "1.66E+00", "0.1660", "17.0%",
     "5 g/wash x 20 washes = 100 g."],
    ["TOTAL", "", "", "", "", "", "0.974", "100%",
     "End-of-life excluded per assignment scope."],
]

story += [app_tbl(data_b)]
story += SP(0.3)

# AI Disclosure
story += [HRFlowable(width="100%", thickness=0.5, color=MGRAY, spaceAfter=6)]
story += [Paragraph(
    "<b>AI Disclosure:</b> Claude (Anthropic, claude-sonnet-4-6) was used as a brainstorming partner "
    "and calculation aid: helping identify relevant BAFU datasets, verifying numerical calculations, "
    "and suggesting how to structure the results. All analytical decisions - including dataset "
    "selection, geographic assumptions, system boundary choices, and interpretation of results - "
    "were made by Omri Shamgar, Tom Ginel, and Tomer Tasa. The written conclusions reflect the students' own understanding "
    "of the material.",
    styles["label"]
)]

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF saved to: {OUT}")
