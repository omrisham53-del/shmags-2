#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tax Incentive Model Generator — v2
National Energy Efficiency Program — EcoTraders

Changes from v1:
- Policy parameter is now a multiplier (e.g. 2 = 20%/yr for 5 yrs), not % year 1
- Degradation factor applied to annual energy savings
- Consolidated to 2 sheets: assumptions + single analysis sheet
- Payback via cumulative NPV crossover, not simple CapEx / savings
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter

# ─── COLORS ───────────────────────────────────────────────────────────────────
F_INPUT   = PatternFill("solid", fgColor="FFFF00")   # yellow  – user input
F_CONTROL = PatternFill("solid", fgColor="FFC000")   # orange  – verify/update
F_HEADING = PatternFill("solid", fgColor="4472C4")   # blue    – section header
F_SUBHEAD = PatternFill("solid", fgColor="BDD7EE")   # l.blue  – col headers
F_RESULT  = PatternFill("solid", fgColor="E2EFDA")   # l.green – results
F_POLICY  = PatternFill("solid", fgColor="FF6B6B")   # red     – key policy row
F_ACCEL   = PatternFill("solid", fgColor="FFF2CC")   # cream   – accel rows
F_NONE    = PatternFill("solid", fgColor="FFFFFF")

FONT_H   = Font(name="Arial", bold=True, color="FFFFFF", size=11)
FONT_SH  = Font(name="Arial", bold=True, color="000000", size=10)
FONT_N   = Font(name="Arial", size=10)
FONT_P   = Font(name="Arial", italic=True, color="FF0000", size=10)
FONT_SM  = Font(name="Arial", italic=True, size=9, color="595959")

A_R = Alignment(horizontal="right",  vertical="center", readingOrder=2)
A_C = Alignment(horizontal="center", vertical="center", readingOrder=2)
A_L = Alignment(horizontal="left",   vertical="center", readingOrder=2)

FMT_NIS = '#,##0 ₪'
FMT_PCT = '0.0%'
FMT_NUM = '#,##0'
FMT_YR  = '0.0'
FMT_X   = '0.0"×"'   # multiplier format: "2.0×"

# ─── SHEET / CELL REFERENCES ──────────────────────────────────────────────────
GLOBAL_SHEET = "נתונים והנחות"
ANALYSIS_SHEET = "ניתוח"

# Must match row layout in build_global_sheet()
TAX_REF  = f"'{GLOBAL_SHEET}'!$F$10"   # corporate tax rate
DISC_REF = f"'{GLOBAL_SHEET}'!$F$11"   # discount rate
ELEC_REF = f"'{GLOBAL_SHEET}'!$F$12"   # electricity price (agorot/kWh)
MULT_REF = f"'{GLOBAL_SHEET}'!$F$15"   # depreciation multiplier (key policy param)

# ─── TECHNOLOGIES ─────────────────────────────────────────────────────────────
TECHS = [
    dict(
        name="משאבות חום (חימום מים)",
        number="3.1",
        lifetime=10,
        savings_pct=0.50,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="החלפת דוד חשמל במשאבת חום | חיסכון ~50% מצריכה | אורך חיים: 10 שנה",
    ),
    dict(
        name="צ'ילרים",
        number="3.2",
        lifetime=17,
        savings_pct=0.20,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="שדרוג מערכת קירור תעשייתית | חיסכון ~20% | אורך חיים: 15-20 שנה",
    ),
    dict(
        name="מדחסי VSD",
        number="3.3",
        lifetime=12,
        savings_pct=0.20,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="מדחסי אוויר עם בקרת מהירות משתנה | חיסכון ~20% | אורך חיים: 10-15 שנה",
    ),
    dict(
        name="מערכות קיטור חשמליות",
        number="3.4",
        lifetime=10,
        savings_pct=0.50,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="החלפת קיטור מבוסס דלק בקיטור חשמלי | חיסכון ~50% מצריכה | אורך חיים: 10 שנה",
    ),
]

MAX_YRS = 20   # year columns: Year 1 … Year 20
# Column 6 = Year 0, Column 7 = Year 1, … Column 6+MAX_YRS = Year MAX_YRS
YR0_COL = 6
MAX_COL_IDX = YR0_COL + MAX_YRS
MAX_COL_LTR = get_column_letter(MAX_COL_IDX)


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def sc(ws, row, col, value=None, fill=None, font=None, align=None, fmt=None):
    c = ws.cell(row=row, column=col)
    if value is not None:
        c.value = value
    if fill:  c.fill = fill
    if font:  c.font = font
    if align: c.alignment = align
    if fmt:   c.number_format = fmt
    return c


def section_hdr(ws, row, label, number=None, col_start=2, col_end=8):
    text = f"{number}. {label}" if number else label
    ws.merge_cells(start_row=row, start_column=col_start,
                   end_row=row, end_column=col_end)
    c = ws.cell(row=row, column=col_start)
    c.value = text
    c.fill  = F_HEADING
    c.font  = FONT_H
    c.alignment = A_R


def subsection_hdr(ws, row, label, col_start=2, col_end=8):
    ws.merge_cells(start_row=row, start_column=col_start,
                   end_row=row, end_column=col_end)
    c = ws.cell(row=row, column=col_start)
    c.value = label
    c.fill  = PatternFill("solid", fgColor="8EA9C1")
    c.font  = Font(name="Arial", bold=True, color="FFFFFF", size=10)
    c.alignment = A_R


def year_header_row(ws, row, max_yrs=MAX_YRS, yr0_label="שנה 0"):
    headers = [(2, "פרמטר"), (3, "יחידות"), (4, "מקור"), (5, "הערות"), (6, yr0_label)]
    for col, val in headers:
        sc(ws, row, col, val, fill=F_SUBHEAD, font=FONT_SH, align=A_C)
    for i in range(1, max_yrs + 1):
        sc(ws, row, 6 + i, f"שנה {i}", fill=F_SUBHEAD, font=FONT_SH, align=A_C)


def set_col_widths(ws, include_year_cols=False):
    ws.column_dimensions['A'].width = 4
    ws.column_dimensions['B'].width = 40
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 18
    if include_year_cols:
        for i in range(1, MAX_YRS + 1):
            ws.column_dimensions[get_column_letter(6 + i)].width = 13


def color_legend(ws, row=1):
    ws.cell(row=row, column=2).value = "מקרא צבעים"
    ws.cell(row=row, column=2).font = FONT_SH
    items = [
        ("ערך להזנה",            F_INPUT),
        ("נתון לעדכון / בקרה",   F_CONTROL),
        ("תוצאת חישוב",          F_NONE),
        ("תוצאות",               F_RESULT),
        ("תמריץ — פחת מואץ",     F_ACCEL),
        ("פרמטר מדיניות מרכזי",  F_POLICY),
    ]
    for i, (label, fill) in enumerate(items):
        r = row + 1 + i
        sc(ws, r, 2, label, fill=fill, font=FONT_N, align=A_R)


# ─── SHEET 1: GLOBAL ASSUMPTIONS ──────────────────────────────────────────────

def build_global_sheet(wb):
    ws = wb.active
    ws.title = GLOBAL_SHEET
    ws.sheet_view.rightToLeft = True
    set_col_widths(ws)

    color_legend(ws, row=1)

    # ── Section 1: Financial Parameters ──
    section_hdr(ws, 9, "פרמטרים פיננסיים", number=1)
    # F10 = tax, F11 = discount, F12 = electricity — refs must match TAX_REF/DISC_REF/ELEC_REF
    fin_rows = [
        (10, "שיעור מס חברות",           "%",          "רשות המסים",   "",
             0.23, F_CONTROL, FMT_PCT),
        (11, "שיעור היוון (יזמי / פרטי)", "%",          "הנחת עבודה",
             "6% לאומי / 10% תעשייתי — ממתין להחלטת דניאל", 0.10, F_INPUT, FMT_PCT),
        (12, 'מחיר חשמל ממוצע לתעשייה', 'אג\'/קוט"ש', "חברת החשמל",
             "ממוצע SMP 2024", 14.0, F_INPUT, '#,##0.0'),
    ]
    for r, label, units, source, notes, val, fill, fmt in fin_rows:
        sc(ws, r, 2, label,  fill=fill, font=FONT_N, align=A_R)
        sc(ws, r, 3, units,  align=A_R)
        sc(ws, r, 4, source, align=A_R)
        sc(ws, r, 5, notes,  align=A_R)
        sc(ws, r, 6, val,    fill=fill, fmt=fmt, align=A_C)

    # ── Section 2: Depreciation Multiplier (key policy parameter) ──
    section_hdr(ws, 14, "פרמטר תמריץ — מכפיל פחת (פחת מואץ)", number=2)
    ws.merge_cells('B14:F14')

    # F15 = multiplier — must match MULT_REF
    sc(ws, 15, 2,
       "מכפיל שיעור הפחת  ←  פרמטר המדיניות המרכזי",
       fill=F_POLICY,
       font=Font(name="Arial", bold=True, size=11, color="FFFFFF"), align=A_R)
    sc(ws, 15, 3, "מכפיל",          fill=F_POLICY, align=A_C,
       font=Font(name="Arial", bold=True, size=11, color="FFFFFF"))
    sc(ws, 15, 4, "פרמטר ניתן לשינוי", align=A_R)
    sc(ws, 15, 5,
       "1.0 = ללא תמריץ (סטנדרטי) | 2.0 = קפריסין (כפול) | 5.0 = 5 שנים",
       fill=F_POLICY, font=Font(name="Arial", italic=True, size=9, color="FFFFFF"), align=A_R)
    sc(ws, 15, 6, 2.0,  # default: 2× (Cyprus model)
       fill=F_INPUT,
       font=Font(name="Arial", bold=True, size=14, color="C00000"),
       fmt=FMT_X, align=A_C)

    ws.cell(row=16, column=2).value = \
        ("מכפיל 2.0 לציוד עם פחת סטנדרטי 10%: שיעור מואץ = 20%/שנה למשך 5 שנים. "
         "סה\"כ ניכוי = 100% CapEx — יתרון הוא קדמות הניכוי (Time Value of Money).")
    ws.cell(row=16, column=2).font = FONT_SM
    ws.merge_cells('B16:F16')

    ws.cell(row=17, column=2).value = \
        ("דוגמאות: מכפיל 1.0 = 10%/שנה ל-10 שנים (סטנדרטי) | "
         "מכפיל 2.0 = 20%/שנה ל-5 שנים | מכפיל 3.33 = 33%/שנה ל-3 שנים | "
         "מכפיל 5.0 = 50%/שנה ל-2 שנים (מודל קפריסין/אירלנד)")
    ws.cell(row=17, column=2).font = FONT_SM
    ws.merge_cells('B17:F17')

    # ── Section 3: Standard Depreciation Rates ──
    section_hdr(ws, 19, "שיעורי פחת סטנדרטיים לפי תקנות מס הכנסה", number=3)
    depr_rows = [
        (20, "משאבות חום",           "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (21, "צ'ילרים ומערכות קירור", "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (22, "מדחסי VSD",            "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (23, "מערכות קיטור",         "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
    ]
    for r, label, units, source, notes, val in depr_rows:
        sc(ws, r, 2, label,  font=FONT_N, align=A_R)
        sc(ws, r, 3, units,  align=A_R)
        sc(ws, r, 4, source, align=A_R)
        sc(ws, r, 5, notes,  align=A_R)
        sc(ws, r, 6, val,    fmt=FMT_PCT, align=A_C)

    ws.cell(row=25, column=2).value = \
        "* שיעורי הפחת לעיל הם הנחות עבודה — יש לוודא מול יועץ מס לפני הגשה"
    ws.cell(row=25, column=2).font = FONT_SM


# ─── SHEET 2: ANALYSIS ────────────────────────────────────────────────────────

def build_analysis_sheet(wb):
    ws = wb.create_sheet(ANALYSIS_SHEET)
    ws.sheet_view.rightToLeft = True
    set_col_widths(ws, include_year_cols=True)

    color_legend(ws, row=1)

    # Title
    ws.merge_cells(start_row=8, start_column=2, end_row=8, end_column=6 + MAX_YRS)
    sc(ws, 8, 2, "ניתוח כלכלי — פחת מואץ לפי טכנולוגיה",
       fill=F_HEADING,
       font=Font(name="Arial", bold=True, color="FFFFFF", size=13), align=A_R)

    # ── Section 1: Financial Parameters reference ──
    section_hdr(ws, 10, "פרמטרים פיננסיים", number=1)
    ref_rows = [
        (11, "שיעור מס חברות",           "%",        TAX_REF,  FMT_PCT,    F_CONTROL),
        (12, "שיעור היוון",               "%",        DISC_REF, FMT_PCT,    F_INPUT),
        (13, 'מחיר חשמל (₪/קוט"ש)',       '₪/קוט"ש', f"={ELEC_REF}/100",
             '#,##0.000', F_INPUT),
    ]
    for r, label, units, ref, fmt, fill in ref_rows:
        sc(ws, r, 2, label,       fill=fill, font=FONT_N, align=A_R)
        sc(ws, r, 3, units,       align=A_R)
        sc(ws, r, 4, GLOBAL_SHEET, align=A_R)
        sc(ws, r, 6, f"={ref}" if not ref.startswith("=") else ref,
           fill=fill, fmt=fmt, align=A_C)

    # fix the electricity price row (already has = prefix from ref_rows)
    ws.cell(row=13, column=6).value = f"={ELEC_REF}/100"

    # ── Section 2: Policy Parameter reference ──
    section_hdr(ws, 15, "פרמטר תמריץ — מכפיל פחת", number=2)
    sc(ws, 16, 2, "מכפיל שיעור הפחת  ←  שנה ב'נתונים והנחות'!F15",
       fill=F_POLICY,
       font=Font(name="Arial", bold=True, size=11, color="FFFFFF"), align=A_R)
    sc(ws, 16, 3, "מכפיל",    fill=F_POLICY,
       font=Font(name="Arial", bold=True, size=11, color="FFFFFF"), align=A_C)
    sc(ws, 16, 4, GLOBAL_SHEET, align=A_R)
    sc(ws, 16, 6, f"={MULT_REF}",
       fill=F_INPUT,
       font=Font(name="Arial", bold=True, size=13, color="C00000"),
       fmt=FMT_X, align=A_C)
    sc(ws, 17, 2,
       "מכפיל × שיעור פחת סטנדרטי = שיעור מואץ | פחת מצטבר = 100% CapEx | "
       "אורך תקופת הפחת = 1 ÷ שיעור מואץ",
       font=FONT_SM, align=A_R)

    # ── Section 3: Technology Analyses ──
    section_hdr(ws, 19, "ניתוחים לפי טכנולוגיה", number=3,
                col_end=6 + MAX_YRS)

    R = 20   # current row pointer
    tech_results = []

    for tech in TECHS:
        R, rmap = _tech_block(ws, tech, R)
        tech_results.append((tech, rmap))
        R += 1  # blank separator row between techs

    # ── Section 4: Summary ──
    R = _summary_block(ws, tech_results, R)

    return ws, tech_results


def _tech_block(ws, tech, R_start):
    """Write one technology's block. Returns (next_free_row, result_row_map)."""
    R = R_start
    tech_end_col = 6 + MAX_YRS

    # Sub-section header
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=tech_end_col)
    sc(ws, R, 2, f"{tech['number']}  {tech['name']}",
       fill=PatternFill("solid", fgColor="1F4E79"),
       font=Font(name="Arial", bold=True, color="FFFFFF", size=11), align=A_R)
    R += 1
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=tech_end_col)
    sc(ws, R, 2, f"* {tech['notes']}",
       font=FONT_SM, align=A_R)
    R += 1

    # ── A: Investment inputs ──────────────────────────────────────────────────
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=tech_end_col)
    sc(ws, R, 2, "א. הנחות בסיסיות להשקעה",
       fill=F_SUBHEAD, font=FONT_SH, align=A_R)
    R += 1

    R_CAPEX  = R;     R += 1
    R_KWH    = R;     R += 1
    R_SVPCT  = R;     R += 1
    R_SVKWH  = R;     R += 1
    R_DEGRAD = R;     R += 1
    R_LIFE   = R;     R += 1
    R_EPRICE = R;     R += 1
    R_SVNIS  = R;     R += 1

    def pending(row, label, units, source, notes):
        sc(ws, row, 2, label,  font=FONT_N, align=A_R)
        sc(ws, row, 3, units,  align=A_R)
        sc(ws, row, 4, source, align=A_R)
        sc(ws, row, 5, notes,  font=FONT_P, align=A_R)
        sc(ws, row, 6, "PENDING", fill=F_INPUT, font=FONT_P, align=A_C)

    pending(R_CAPEX, "עלות השקעה (CapEx)", "₪", "נתוני רפי",
            "⚠ ממתין לנתוני ראש המהנדסים")
    pending(R_KWH, "צריכת אנרגיה שנתית (לפני החלפה)", 'קוט"ש/שנה', "נתוני רפי",
            "⚠ ממתין לנתוני ראש המהנדסים")

    sc(ws, R_SVPCT, 2, "חיסכון אנרגטי",     font=FONT_N, align=A_R)
    sc(ws, R_SVPCT, 3, "% מצריכה",           align=A_R)
    sc(ws, R_SVPCT, 4, "ממצאי הנדסה",        align=A_R)
    sc(ws, R_SVPCT, 6, tech['savings_pct'],   fill=F_CONTROL, fmt=FMT_PCT, align=A_C)

    sc(ws, R_SVKWH, 2, 'חיסכון שנתי בסיסי', font=FONT_N, align=A_R)
    sc(ws, R_SVKWH, 3, 'קוט"ש/שנה',          align=A_R)
    sc(ws, R_SVKWH, 4, "חישוב",               align=A_R)
    sc(ws, R_SVKWH, 5, "= צריכה × שיעור חיסכון", align=A_R)
    sc(ws, R_SVKWH, 6,
       f"=IF(ISNUMBER($F${R_KWH}),$F${R_KWH}*$F${R_SVPCT},\"PENDING\")",
       fmt=FMT_NUM, align=A_C)

    sc(ws, R_DEGRAD, 2, "גורם שחיקת ביצועים", font=FONT_N, align=A_R)
    sc(ws, R_DEGRAD, 3, "% לשנה",              align=A_R)
    sc(ws, R_DEGRAD, 4, "הנחת עבודה",          align=A_R)
    sc(ws, R_DEGRAD, 5,
       "ירידה שנתית בחיסכון | טווח: 0.5%-1.0%/שנה — לאשר מול רפי",
       font=FONT_P, align=A_R)
    sc(ws, R_DEGRAD, 6, 0.005,  # 0.5% default — pending Rafi data
       fill=F_INPUT, fmt=FMT_PCT, align=A_C)

    sc(ws, R_LIFE, 2, "אורך חיי הציוד (כלכלי)", font=FONT_N, align=A_R)
    sc(ws, R_LIFE, 3, "שנים",                    align=A_R)
    sc(ws, R_LIFE, 4, "ממצאי הנדסה",             align=A_R)
    sc(ws, R_LIFE, 6, tech['lifetime'], fill=F_CONTROL, fmt=FMT_YR, align=A_C)

    sc(ws, R_EPRICE, 2, 'מחיר חשמל',    font=FONT_N, align=A_R)
    sc(ws, R_EPRICE, 3, '₪/קוט"ש',      align=A_R)
    sc(ws, R_EPRICE, 4, "גיליון הנחות", align=A_R)
    sc(ws, R_EPRICE, 6, f"={ELEC_REF}/100", fmt='#,##0.000', align=A_C)

    sc(ws, R_SVNIS, 2, 'חיסכון שנתי בסיסי (₪, שנה 1)', font=FONT_N, align=A_R)
    sc(ws, R_SVNIS, 3, '₪/שנה',                          align=A_R)
    sc(ws, R_SVNIS, 4, "חישוב",                           align=A_R)
    sc(ws, R_SVNIS, 5, '= חיסכון קוט"ש × מחיר חשמל',    align=A_R)
    sc(ws, R_SVNIS, 6,
       f"=IF(ISNUMBER($F${R_SVKWH}),$F${R_SVKWH}*$F${R_EPRICE},\"PENDING\")",
       fmt=FMT_NIS, align=A_C)

    R += 1  # blank row

    # ── B: Depreciation schedules ─────────────────────────────────────────────
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=tech_end_col)
    sc(ws, R, 2, "ב. לוחות פחת — השוואה (ללא תמריץ vs. עם מכפיל)",
       fill=F_SUBHEAD, font=FONT_SH, align=A_R)
    R += 1

    year_header_row(ws, R, yr0_label="שנה 0 (השקעה)")
    R_DH = R;  R += 1

    R_SD = R;  R += 1   # standard depreciation
    R_ST = R;  R += 1   # standard tax shield
    R_AD = R;  R += 1   # accel depreciation
    R_AT = R;  R += 1   # accel tax shield

    # labels
    for rr, lbl, fill in [
        (R_SD, "פחת שנתי — סטנדרטי",   F_NONE),
        (R_ST, "מגן מס — סטנדרטי",     F_RESULT),
        (R_AD, "פחת שנתי — מואץ",      F_ACCEL),
        (R_AT, "מגן מס — מואץ",        F_ACCEL),
    ]:
        sc(ws, rr, 2, lbl,  fill=fill, font=FONT_N, align=A_R)
        sc(ws, rr, 3, "₪",   align=A_R)
        sc(ws, rr, 4, "חישוב", align=A_R)
        sc(ws, rr, 6, 0,    fill=fill, fmt=FMT_NIS, align=A_C)

    sc(ws, R_SD, 5,
       f"= CapEx × {tech['std_depr_pct']:.0%} | קו ישר | עד שנה {tech['std_depr_yrs']}",
       align=A_R)
    sc(ws, R_ST, 5, "= פחת × שיעור מס", align=A_R)
    sc(ws, R_AD, 5,
       "= CapEx × (שיעור סטנדרטי × מכפיל) | תקופה = 1 ÷ שיעור מואץ",
       align=A_R)
    sc(ws, R_AT, 5, "= פחת מואץ × שיעור מס", align=A_R)

    capex_f  = f"$F${R_CAPEX}"
    std_r_f  = str(tech['std_depr_pct'])   # hardcoded rate; changes only if policy changes
    tax_f    = f"={TAX_REF}"               # will be used inline
    disc_f   = f"={DISC_REF}"
    mult_f   = f"$F$16"   # local reference to Section 2 display cell on this sheet
    svnis_f  = f"$F${R_SVNIS}"
    degrad_f = f"$F${R_DEGRAD}"
    life_n   = tech['lifetime']
    std_yrs  = tech['std_depr_yrs']

    # For depreciation formulas, reference the global sheet directly
    TAX_INLINE  = TAX_REF
    MULT_INLINE = MULT_REF

    for i in range(1, MAX_YRS + 1):
        col = 6 + i
        cl  = get_column_letter(col)

        # Standard depreciation: flat CapEx × std_rate for std_depr_yrs years
        if i <= std_yrs:
            sd = f"=IF(ISNUMBER({capex_f}),{capex_f}*{std_r_f},0)"
        else:
            sd = "=0"
        sc(ws, R_SD, col, sd, fill=F_NONE, fmt=FMT_NIS, align=A_C)

        # Standard tax shield
        sc(ws, R_ST, col,
           f"={cl}{R_SD}*{TAX_INLINE}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)

        # Accelerated depreciation — multiplier model:
        # accel_rate = std_rate × multiplier
        # Year qualifies if i <= ROUND(1 / accel_rate, 0)
        # Amount per qualifying year = CapEx × accel_rate
        ad = (
            f"=IF(ISNUMBER({capex_f}),"
            f"IF({i}<=ROUND(1/({std_r_f}*{MULT_INLINE}),0),"
            f"{capex_f}*{std_r_f}*{MULT_INLINE},0),0)"
        )
        sc(ws, R_AD, col, ad, fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

        # Accelerated tax shield
        sc(ws, R_AT, col,
           f"={cl}{R_AD}*{TAX_INLINE}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

    R += 1  # blank row

    # ── C: Cash Flow Analysis ─────────────────────────────────────────────────
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=tech_end_col)
    sc(ws, R, 2, "ג. ניתוח תזרים מזומנים",
       fill=F_SUBHEAD, font=FONT_SH, align=A_R)
    R += 1

    year_header_row(ws, R, yr0_label="שנה 0 (השקעה)")
    R += 1

    R_INV = R;  R += 1   # investment
    R_ESV = R;  R += 1   # energy savings (degraded)
    R_SN  = R;  R += 1   # std net CF
    R_SD2 = R;  R += 1   # std discounted CF
    R_SC  = R;  R += 1   # std cumulative NPV
    R_AN  = R;  R += 1   # accel net CF
    R_AD2 = R;  R += 1   # accel discounted CF
    R_AC  = R;  R += 1   # accel cumulative NPV

    for rr, lbl, fill in [
        (R_INV, "השקעה ראשונית (CapEx)",         F_NONE),
        (R_ESV, "חיסכון שנתי — אנרגיה (בניכוי שחיקה)", F_NONE),
        (R_SN,  "תזרים נקי — ללא תמריץ",         F_NONE),
        (R_SD2, "תזרים מהוון — ללא תמריץ",        F_RESULT),
        (R_SC,  "NPV מצטבר — ללא תמריץ",         F_RESULT),
        (R_AN,  "תזרים נקי — עם תמריץ",          F_ACCEL),
        (R_AD2, "תזרים מהוון — עם תמריץ",         F_ACCEL),
        (R_AC,  "NPV מצטבר — עם תמריץ",          F_ACCEL),
    ]:
        sc(ws, rr, 2, lbl, fill=fill, font=FONT_N, align=A_R)
        sc(ws, rr, 3, "₪",  align=A_R)
        sc(ws, rr, 4, "חישוב", align=A_R)

    # Year 0 column
    sc(ws, R_INV, 6, f"=IF(ISNUMBER({capex_f}),-{capex_f},\"PENDING\")",
       fmt=FMT_NIS, align=A_C)
    for rr in [R_ESV, R_SN, R_AN]:
        sc(ws, rr, 6, 0, fmt=FMT_NIS, align=A_C)
    sc(ws, R_SD2, 6, f"=F{R_SN}",  fill=F_RESULT, fmt=FMT_NIS, align=A_C)
    sc(ws, R_SC,  6, f"=F{R_SD2}", fill=F_RESULT, fmt=FMT_NIS, align=A_C)
    sc(ws, R_AD2, 6, f"=F{R_AN}",  fill=F_ACCEL,  fmt=FMT_NIS, align=A_C)
    sc(ws, R_AC,  6, f"=F{R_AD2}", fill=F_ACCEL,  fmt=FMT_NIS, align=A_C)

    for i in range(1, MAX_YRS + 1):
        col = 6 + i
        cl  = get_column_letter(col)
        pcl = get_column_letter(col - 1)

        # Energy savings with degradation: base × (1 - degrad)^(year-1)
        if i <= life_n:
            esv = (f"=IF(ISNUMBER({svnis_f}),"
                   f"{svnis_f}*(1-{degrad_f})^{i-1},0)")
        else:
            esv = "=0"
        sc(ws, R_ESV, col, esv, fmt=FMT_NIS, align=A_C)

        # Std net = energy savings + std tax shield
        sc(ws, R_SN, col,
           f"={cl}{R_ESV}+{cl}{R_ST}",
           fmt=FMT_NIS, align=A_C)

        # Std discounted
        sc(ws, R_SD2, col,
           f"={cl}{R_SN}/(1+{DISC_REF})^{i}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)

        # Std cumulative
        sc(ws, R_SC, col,
           f"={pcl}{R_SC}+{cl}{R_SD2}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)

        # Accel net = energy savings + accel tax shield
        sc(ws, R_AN, col,
           f"={cl}{R_ESV}+{cl}{R_AT}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

        # Accel discounted
        sc(ws, R_AD2, col,
           f"={cl}{R_AN}/(1+{DISC_REF})^{i}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

        # Accel cumulative
        sc(ws, R_AC, col,
           f"={pcl}{R_AC}+{cl}{R_AD2}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

    R += 1  # blank row

    # ── D: Results ────────────────────────────────────────────────────────────
    ws.merge_cells(start_row=R, start_column=2, end_row=R, end_column=8)
    sc(ws, R, 2, "ד. תוצאות",
       fill=F_SUBHEAD, font=FONT_SH, align=A_R)
    R += 1

    YR0 = get_column_letter(YR0_COL)   # F

    def result_row(ws, row, label, formula, fmt, fill=F_RESULT):
        sc(ws, row, 2, label,   fill=fill,
           font=Font(name="Arial", bold=True, size=10), align=A_R)
        if "₪" in fmt:
            unit = 'ש"ח'
        elif "%" in fmt:
            unit = "%"
        else:
            unit = "שנים"
        sc(ws, row, 3, unit, align=A_R)
        sc(ws, row, 6, formula, fill=fill, fmt=fmt, align=A_C)

    R_NPV_S = R;  R += 1
    R_NPV_A = R;  R += 1
    R_DNPV  = R;  R += 1
    R += 1  # blank
    R_ROI_S = R;  R += 1
    R_ROI_A = R;  R += 1
    R_DROI  = R;  R += 1
    R += 1  # blank
    R_PBK_S = R;  R += 1
    R_PBK_A = R;  R += 1

    # NPV = sum of discounted cash flows (Year 0 already discounted = same as undiscounted for i=0)
    result_row(ws, R_NPV_S, "NPV ללא תמריץ",
               f"=SUM({YR0}{R_SD2}:{MAX_COL_LTR}{R_SD2})", FMT_NIS)
    result_row(ws, R_NPV_A, "NPV עם תמריץ",
               f"=SUM({YR0}{R_AD2}:{MAX_COL_LTR}{R_AD2})", FMT_NIS, F_ACCEL)
    result_row(ws, R_DNPV, "דלתא NPV — ערך התמריץ",
               f"=F{R_NPV_A}-F{R_NPV_S}", FMT_NIS, F_INPUT)

    result_row(ws, R_ROI_S, "ROI ללא תמריץ",
               f"=IF(ISNUMBER({capex_f}),"
               f"(SUM({YR0}{R_SD2}:{MAX_COL_LTR}{R_SD2})+{capex_f})/{capex_f},"
               f"\"PENDING\")",
               FMT_PCT)
    result_row(ws, R_ROI_A, "ROI עם תמריץ",
               f"=IF(ISNUMBER({capex_f}),"
               f"(SUM({YR0}{R_AD2}:{MAX_COL_LTR}{R_AD2})+{capex_f})/{capex_f},"
               f"\"PENDING\")",
               FMT_PCT, F_ACCEL)
    result_row(ws, R_DROI, "שיפור ROI בזכות התמריץ",
               f"=IF(ISNUMBER(F{R_ROI_A}),F{R_ROI_A}-F{R_ROI_S},\"PENDING\")",
               FMT_PCT, F_INPUT)

    # Payback via cumulative NPV crossover (linear interpolation)
    # cumulative NPV range: F{R_SC}:{MAX_COL_LTR}{R_SC} (Year 0 through Year 20)
    # MATCH finds first position where cumulative > 0; position 1 = Year 0
    # payback_year = (position - 1) but accounting for year 0 offset
    # Linear interpolation: fractional year = abs(prev) / (next - prev)
    def pbk_formula(R_cumul):
        rng = f"{YR0}{R_cumul}:{MAX_COL_LTR}{R_cumul}"
        return (
            f"=IFERROR("
            f"MATCH(1,({rng}>0)*1,0)-2+"
            f"ABS(INDEX({rng},MATCH(1,({rng}>0)*1,0)-1))/"
            f"(INDEX({rng},MATCH(1,({rng}>0)*1,0))-"
            f"INDEX({rng},MATCH(1,({rng}>0)*1,0)-1)),"
            f"\"לא מגיע לפירעון\")"
        )

    result_row(ws, R_PBK_S, "תקופת החזר — ללא תמריץ (NPV)",
               pbk_formula(R_SC), FMT_YR)
    result_row(ws, R_PBK_A, "תקופת החזר — עם תמריץ (NPV)",
               pbk_formula(R_AC), FMT_YR, F_ACCEL)

    sc(ws, R_PBK_A + 1, 2,
       "* תקופת ההחזר מחושבת לפי נקודת הקרוסאובר של ה-NPV המצטבר (אינטרפולציה לינארית)",
       font=FONT_SM, align=A_R)

    return R_PBK_A + 3, dict(
        npv_std=R_NPV_S, npv_acc=R_NPV_A, d_npv=R_DNPV,
        roi_std=R_ROI_S, roi_acc=R_ROI_A, d_roi=R_DROI,
        pbk_std=R_PBK_S, pbk_acc=R_PBK_A,
    )


def _summary_block(ws, tech_results, R_start):
    R = R_start
    section_hdr(ws, R, "סיכום השוואתי לפי טכנולוגיה", number=4, col_end=12)
    R += 1

    sc(ws, R, 2,
       f"* פרמטר המדיניות (מכפיל פחת) = '{GLOBAL_SHEET}'!F15 — שנה שם ותוצאות מתעדכנות אוטומטית",
       font=FONT_SM, align=A_R)
    R += 1

    hdrs = [
        (2, "טכנולוגיה"),
        (3, "NPV ללא תמריץ"),
        (4, "NPV עם תמריץ"),
        (5, "דלתא NPV"),
        (6, "ROI ללא"),
        (7, "ROI עם"),
        (8, "שיפור ROI"),
        (9, "החזר ללא (שנים)"),
        (10, "החזר עם (שנים)"),
    ]
    for col, lbl in hdrs:
        sc(ws, R, col, lbl, fill=F_SUBHEAD, font=FONT_SH, align=A_C)
    R += 1

    for tech, rmap in tech_results:
        sn = ANALYSIS_SHEET
        sc(ws, R, 2, tech['name'], font=FONT_N, align=A_R)
        for col, key, fmt, fill in [
            (3, 'npv_std', FMT_NIS, F_RESULT),
            (4, 'npv_acc', FMT_NIS, F_ACCEL),
            (5, 'd_npv',   FMT_NIS, F_INPUT),
            (6, 'roi_std', FMT_PCT, F_RESULT),
            (7, 'roi_acc', FMT_PCT, F_ACCEL),
            (8, 'd_roi',   FMT_PCT, F_INPUT),
            (9, 'pbk_std', FMT_YR,  F_RESULT),
            (10, 'pbk_acc', FMT_YR, F_ACCEL),
        ]:
            sc(ws, R, col, f"=$F${rmap[key]}",
               fill=fill, fmt=fmt, align=A_C)
        R += 1

    sc(ws, R + 1, 2,
       "** CapEx וצריכת אנרגיה שנתית ממתינים לנתוני רפי — לאחר הזנתם כל התוצאות יתעדכנו אוטומטית",
       font=Font(name="Arial", italic=True, color="FF0000", size=9), align=A_R)

    return R + 3


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    wb = openpyxl.Workbook()
    build_global_sheet(wb)
    build_analysis_sheet(wb)

    out = "/home/user/shmags-2/projects/energy-program/tax_incentive_model.xlsx"
    wb.save(out)
    print(f"Saved: {out}")
    print("Sheets:", [ws.title for ws in wb.worksheets])


if __name__ == "__main__":
    main()
