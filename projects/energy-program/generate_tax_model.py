#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tax Incentive Model Generator
National Energy Efficiency Program - EcoTraders
Compares NPV/ROI with and without accelerated depreciation (פחת מואץ)
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter

# ─── COLORS ──────────────────────────────────────────────────────────────────
F_INPUT    = PatternFill("solid", fgColor="FFFF00")   # yellow  – user input
F_CONTROL  = PatternFill("solid", fgColor="FFC000")   # orange  – verify/update
F_HEADING  = PatternFill("solid", fgColor="4472C4")   # blue    – section header
F_SUBHEAD  = PatternFill("solid", fgColor="BDD7EE")   # l.blue  – col headers / sub
F_RESULT   = PatternFill("solid", fgColor="E2EFDA")   # l.green – results
F_POLICY   = PatternFill("solid", fgColor="FF0000")   # red     – the flex param row
F_ACCEL    = PatternFill("solid", fgColor="FFF2CC")   # cream   – accel incentive rows
F_NONE     = PatternFill("solid", fgColor="FFFFFF")

FONT_H   = Font(name="Arial", bold=True, color="FFFFFF", size=11)
FONT_SH  = Font(name="Arial", bold=True, color="000000", size=10)
FONT_N   = Font(name="Arial", size=10)
FONT_P   = Font(name="Arial", italic=True, color="FF0000", size=10)  # pending

A_R   = Alignment(horizontal="right",  vertical="center", readingOrder=2)
A_C   = Alignment(horizontal="center", vertical="center", readingOrder=2)
A_L   = Alignment(horizontal="left",   vertical="center", readingOrder=2)

FMT_NIS = '#,##0 ₪'
FMT_PCT = '0.0%'
FMT_NUM = '#,##0'
FMT_YR  = '0.0'

# ─── GLOBAL CELL REFERENCES (must match build_global_sheet row layout) ────────
# F10 = tax rate, F11 = discount rate, F12 = electricity price (agorot/kWh)
TAX_REF   = "'נתונים והנחות - כללי'!$F$10"
DISC_REF  = "'נתונים והנחות - כללי'!$F$11"
ELEC_REF  = "'נתונים והנחות - כללי'!$F$12"   # agorot/kWh — divide by 100 for ₪/kWh
ACCEL_REF = "'פרמטרי תמריץ'!$F$10"           # the key policy slider (row 10)

# ─── TECHNOLOGIES ─────────────────────────────────────────────────────────────
TECHS = [
    dict(
        name="משאבות חום (חימום מים)",
        sheet="ניתוח - משאבות חום",
        lifetime=10,
        savings_pct=0.50,
        std_depr_pct=0.10,   # 10%/yr straight-line (Israeli tax: machinery)
        std_depr_yrs=10,
        notes="החלפת דוד חשמל במשאבת חום | חיסכון ~50% מצריכה",
    ),
    dict(
        name="צ'ילרים",
        sheet="ניתוח - צ'ילרים",
        lifetime=17,          # 17.5 → round to 17 for integer year columns
        savings_pct=0.20,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="שדרוג מערכת קירור תעשייתית | חיסכון ~20% | טווח: 15–20 שנה",
    ),
    dict(
        name="מדחסי VSD",
        sheet="ניתוח - מדחסי VSD",
        lifetime=12,          # 12.5 → round to 12
        savings_pct=0.20,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="מדחסי אוויר עם בקרת מהירות משתנה | חיסכון ~20% | טווח: 10–15 שנה",
    ),
    dict(
        name="מערכות קיטור חשמליות",
        sheet="ניתוח - קיטור חשמלי",
        lifetime=10,
        savings_pct=0.50,
        std_depr_pct=0.10,
        std_depr_yrs=10,
        notes="החלפת קיטור מבוסס דלק בקיטור חשמלי | חיסכון ~50% מצריכה",
    ),
]

MAX_YRS = 20   # number of year columns (Year 1 … Year 20)


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def sc(ws, row, col, value=None, fill=None, font=None, align=None, fmt=None):
    c = ws.cell(row=row, column=col)
    if value is not None:
        c.value = value
    if fill:  c.fill  = fill
    if font:  c.font  = font
    if align: c.alignment = align
    if fmt:   c.number_format = fmt
    return c


def section_hdr(ws, row, label, number=None, col_start=2, col_end=8):
    text = f"{number}. {label}" if number else label
    ws.merge_cells(start_row=row, start_column=col_start, end_row=row, end_column=col_end)
    c = ws.cell(row=row, column=col_start)
    c.value = text
    c.fill  = F_HEADING
    c.font  = FONT_H
    c.alignment = A_R


def color_legend(ws, row=1):
    ws.cell(row=row, column=2).value = "מקרא צבעים"
    ws.cell(row=row, column=2).font  = FONT_SH
    items = [
        ("ערך להזנה",              F_INPUT),
        ("נתונים לעדכון / בקרה",   F_CONTROL),
        ("כותרות משנה",            F_SUBHEAD),
        ("תוצאת חישוב / טקסט",     F_NONE),
        ("תוצאות",                 F_RESULT),
        ("שורת תמריץ",             F_ACCEL),
    ]
    for i, (label, fill) in enumerate(items):
        r = row + 1 + i
        ws.cell(row=r, column=2).value = label
        ws.cell(row=r, column=2).fill  = fill
        ws.cell(row=r, column=2).font  = FONT_N
        ws.cell(row=r, column=2).alignment = A_R


def set_col_widths(ws, extra_cols=0):
    ws.column_dimensions['A'].width = 4
    ws.column_dimensions['B'].width = 38
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 28
    ws.column_dimensions['F'].width = 18
    for i in range(1, extra_cols + 1):
        ws.column_dimensions[get_column_letter(6 + i)].width = 14


def year_header_row(ws, row, max_yrs, label_b="פרמטר", label_c="יחידות", label_d="מקור", label_e="הערות", yr0_label="שנה 0"):
    headers = [(2, label_b), (3, label_c), (4, label_d), (5, label_e), (6, yr0_label)]
    for col, val in headers:
        sc(ws, row, col, val, fill=F_SUBHEAD, font=FONT_SH, align=A_C)
    for i in range(1, max_yrs + 1):
        sc(ws, row, 6 + i, f"שנה {i}", fill=F_SUBHEAD, font=FONT_SH, align=A_C)


# ─── SHEET 1: GLOBAL ASSUMPTIONS ──────────────────────────────────────────────

def build_global_sheet(wb):
    ws = wb.active
    ws.title = "נתונים והנחות - כללי"
    ws.sheet_view.rightToLeft = True
    set_col_widths(ws)

    color_legend(ws, row=1)

    # Section 1: Financial parameters
    section_hdr(ws, 9, "פרמטרים פיננסיים", number=1)
    # ROW 10 = tax rate  (must match TAX_REF → $F$10)
    # ROW 11 = discount  (must match DISC_REF → $F$11)
    # ROW 12 = elec price (must match ELEC_REF → $F$12)
    rows = [
        (10, "שיעור מס חברות",             "%",          "רשות המסים",     "",                                          0.23,  F_CONTROL, FMT_PCT),
        (11, "שיעור היוון - יזמי / פרטי",   "%",          "הנחת עבודה",     "6% לאומי / 10% תעשייתי — ממתין להחלטת דניאל", 0.10,  F_INPUT,   FMT_PCT),
        (12, "מחיר חשמל ממוצע לתעשייה",    "אג׳/קוט\"ש", "חברת החשמל",    "ממוצע SMP 2024",                            14.0,  F_INPUT,   '#,##0.0'),
    ]
    for r, label, units, source, notes, val, fill, fmt in rows:
        sc(ws, r, 2, label, fill=fill, font=FONT_N, align=A_R)
        sc(ws, r, 3, units, align=A_R)
        sc(ws, r, 4, source, align=A_R)
        sc(ws, r, 5, notes,  align=A_R)
        sc(ws, r, 6, val,    fill=fill, fmt=fmt, align=A_C)

    # Section 2: Standard depreciation rates (Israeli tax regulations)
    section_hdr(ws, 14, "שיעורי פחת סטנדרטיים לפי תקנות מס הכנסה", number=2)
    depr_rows = [
        (15, "משאבות חום",            "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (16, "צ'ילרים ומערכות קירור", "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (17, "מדחסי VSD",             "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
        (18, "מערכות קיטור",          "% לשנה", "תקנות פחת", "ציוד מכני",  0.10),
    ]
    for r, label, units, source, notes, val in depr_rows:
        sc(ws, r, 2, label, font=FONT_N, align=A_R)
        sc(ws, r, 3, units, align=A_R)
        sc(ws, r, 4, source, align=A_R)
        sc(ws, r, 5, notes,  align=A_R)
        sc(ws, r, 6, val,    fmt=FMT_PCT, align=A_C)

    ws.cell(row=20, column=2).value = "* שיעורי הפחת לעיל הם הנחות עבודה — יש לוודא מול יועץ מס לפני הגשה"
    ws.cell(row=20, column=2).font = Font(name="Arial", italic=True, size=9, color="595959")


# ─── SHEET 2: POLICY PARAMETERS ───────────────────────────────────────────────

def build_policy_sheet(wb):
    ws = wb.create_sheet("פרמטרי תמריץ")
    ws.sheet_view.rightToLeft = True
    set_col_widths(ws)

    color_legend(ws, row=1)

    ws.merge_cells('B8:F8')
    sc(ws, 8, 2, "פרמטרי פחת מואץ — מדיניות", fill=F_HEADING, font=FONT_H, align=A_R)

    # ROW 10 = the policy slider — ACCEL_REF must point here
    ws.merge_cells('B9:E9')
    sc(ws, 9, 2,
       "שנה את הערך בתא F10 כדי לשנות את שיעור הפחת המואץ בשנה הראשונה. "
       "הערך מוזן פעם אחת כאן ומשפיע על כל ארבעת הניתוחים.",
       font=Font(name="Arial", italic=True, size=9, color="595959"), align=A_R)

    sc(ws, 10, 2, "שיעור פחת מואץ בשנה 1  ← פרמטר המדיניות המרכזי",
       fill=F_POLICY, font=Font(name="Arial", bold=True, size=11, color="FFFFFF"), align=A_R)
    sc(ws, 10, 3, "%",      align=A_R)
    sc(ws, 10, 4, "פרמטר ניתן לשינוי", align=A_R)
    sc(ws, 10, 5, "0% = ללא תמריץ | 100% = מחיקה מלאה בשנה 1 (מודל אירלנד / קנדה / סינגפור)", align=A_R)
    sc(ws, 10, 6, 1.0,   # default: 100%
       fill=F_INPUT, font=Font(name="Arial", bold=True, size=13, color="C00000"),
       fmt=FMT_PCT, align=A_C)

    # Reference table of international benchmarks
    section_hdr(ws, 12, "תרחישים לדוגמא — דגמים בינלאומיים", number=2)
    scenarios = [
        (13, "אירלנד ACA / קנדה AII / סינגפור s.19A", "100%",  "מחיקה מלאה בשנה 1"),
        (14, "ספרד — פחת חופשי",                        "100%",  "עד 500K EUR, 2023–2024 בלבד"),
        (15, "קפריסין — מכפיל 2× (אנרגיה סולארית)",     "מכפיל", "200% מהפחת הרגיל"),
        (16, "תרחיש 3 שנים",                            "33%",   "פריסה שווה — שנה 1–3"),
        (17, "תרחיש 5 שנים",                            "20%",   "פריסה שווה — שנה 1–5"),
        (18, "ללא תמריץ (סטנדרטי)",                     "0%",    "פחת לפי אורך חיי הציוד (10% לשנה)"),
    ]
    for r, country, rate, note in scenarios:
        sc(ws, r, 2, country, font=FONT_N, align=A_R)
        sc(ws, r, 3, rate, align=A_C)
        sc(ws, r, 4, note,    align=A_R)

    ws.cell(row=20, column=2).value = \
        "* שנה 2 ואילך: יתרת עלות הרכישה (CapEx × (1 − שיעור מואץ)) מופחתת בקו ישר על יתרת שנות אורך החיים הרגיל"
    ws.cell(row=20, column=2).font = Font(name="Arial", italic=True, size=9, color="595959")


# ─── TECHNOLOGY ANALYSIS SHEET ────────────────────────────────────────────────

def build_tech_sheet(wb, tech):
    ws = wb.create_sheet(tech['sheet'])
    ws.sheet_view.rightToLeft = True
    set_col_widths(ws, extra_cols=MAX_YRS)

    color_legend(ws, row=1)

    # Title
    ws.merge_cells(start_row=8, start_column=2, end_row=8, end_column=6 + MAX_YRS)
    sc(ws, 8, 2, f"ניתוח כלכלי — {tech['name']}",
       fill=F_HEADING, font=Font(name="Arial", bold=True, color="FFFFFF", size=13), align=A_R)
    sc(ws, 9, 2, f"* {tech['notes']}",
       font=Font(name="Arial", italic=True, size=9, color="595959"), align=A_R)

    R = 11   # current row pointer

    # ── SECTION 1: INVESTMENT ASSUMPTIONS ──────────────────────────────────────
    section_hdr(ws, R, "הנחות בסיסיות להשקעה", number=1, col_end=6 + MAX_YRS)
    R_CAPEX      = R + 1
    R_KWH        = R + 2
    R_SVPCT      = R + 3
    R_SVKWH      = R + 4
    R_LIFE       = R + 5
    R_EPRICE     = R + 6
    R_SVNIS      = R + 7

    def pending_row(ws, row, label, units, source, notes):
        sc(ws, row, 2, label,    font=FONT_N, align=A_R)
        sc(ws, row, 3, units,    align=A_R)
        sc(ws, row, 4, source,   align=A_R)
        sc(ws, row, 5, notes,    font=FONT_P, align=A_R)
        sc(ws, row, 6, "PENDING", fill=F_INPUT, font=FONT_P, align=A_C)

    pending_row(ws, R_CAPEX, "עלות השקעה (CapEx)", "₪",
                "נתוני רפי", "⚠ ממתין לנתוני ראש המהנדסים")
    pending_row(ws, R_KWH, "צריכת אנרגיה שנתית (לפני החלפה)", 'קוט"ש/שנה',
                "נתוני רפי", "⚠ ממתין לנתוני ראש המהנדסים")

    sc(ws, R_SVPCT, 2, "חיסכון אנרגטי", font=FONT_N, align=A_R)
    sc(ws, R_SVPCT, 3, "% מצריכה",       align=A_R)
    sc(ws, R_SVPCT, 4, "ממצאי הנדסה",    align=A_R)
    sc(ws, R_SVPCT, 6, tech['savings_pct'], fill=F_CONTROL, fmt=FMT_PCT, align=A_C)

    sc(ws, R_SVKWH, 2, 'חיסכון שנתי בצריכת חשמל', font=FONT_N, align=A_R)
    sc(ws, R_SVKWH, 3, 'קוט"ש/שנה',                align=A_R)
    sc(ws, R_SVKWH, 4, "חישוב",                     align=A_R)
    sc(ws, R_SVKWH, 5, "= צריכה × שיעור חיסכון",   align=A_R)
    sc(ws, R_SVKWH, 6,
       f"=IF(ISNUMBER($F${R_KWH}),$F${R_KWH}*$F${R_SVPCT},\"PENDING\")",
       fmt=FMT_NUM, align=A_C)

    sc(ws, R_LIFE, 2, "אורך חיי הציוד (כלכלי)", font=FONT_N, align=A_R)
    sc(ws, R_LIFE, 3, "שנים",                    align=A_R)
    sc(ws, R_LIFE, 4, "ממצאי הנדסה",             align=A_R)
    sc(ws, R_LIFE, 6, tech['lifetime'], fill=F_CONTROL, fmt=FMT_YR, align=A_C)

    sc(ws, R_EPRICE, 2, 'מחיר חשמל', font=FONT_N, align=A_R)
    sc(ws, R_EPRICE, 3, '₪/קוט"ש',   align=A_R)
    sc(ws, R_EPRICE, 4, "גיליון הנחות", align=A_R)
    sc(ws, R_EPRICE, 6, f"={ELEC_REF}/100", fmt='#,##0.000', align=A_C)

    sc(ws, R_SVNIS, 2, 'חיסכון שנתי (₪)', font=FONT_N, align=A_R)
    sc(ws, R_SVNIS, 3, '₪/שנה',            align=A_R)
    sc(ws, R_SVNIS, 4, "חישוב",             align=A_R)
    sc(ws, R_SVNIS, 5, '= חיסכון קוט"ש × מחיר חשמל', align=A_R)
    sc(ws, R_SVNIS, 6,
       f"=IF(ISNUMBER($F${R_SVKWH}),$F${R_SVKWH}*$F${R_EPRICE},\"PENDING\")",
       fmt=FMT_NIS, align=A_C)

    R = R_SVNIS + 2

    # ── SECTION 2: FINANCIAL ASSUMPTIONS ───────────────────────────────────────
    section_hdr(ws, R, "הנחות פיננסיות", number=2, col_end=6 + MAX_YRS)
    R_TAX  = R + 1
    R_DISC = R + 2
    R_SDPR = R + 3   # std depreciation rate

    for row, label, ref, fmt in [
        (R_TAX,  "שיעור מס חברות",  TAX_REF,  FMT_PCT),
        (R_DISC, "שיעור היוון",      DISC_REF, FMT_PCT),
    ]:
        sc(ws, row, 2, label,           font=FONT_N, align=A_R)
        sc(ws, row, 3, "%",             align=A_R)
        sc(ws, row, 4, "גיליון הנחות", align=A_R)
        sc(ws, row, 6, f"={ref}",       fmt=fmt, align=A_C)

    sc(ws, R_SDPR, 2, "שיעור פחת סטנדרטי", font=FONT_N, align=A_R)
    sc(ws, R_SDPR, 3, "%/שנה",              align=A_R)
    sc(ws, R_SDPR, 4, "תקנות מס הכנסה",    align=A_R)
    sc(ws, R_SDPR, 5, f"קו ישר — {tech['std_depr_yrs']} שנים", align=A_R)
    sc(ws, R_SDPR, 6, tech['std_depr_pct'], fill=F_CONTROL, fmt=FMT_PCT, align=A_C)

    R = R_SDPR + 2

    # ── SECTION 3: POLICY PARAMETER ────────────────────────────────────────────
    section_hdr(ws, R, "פרמטר המדיניות — פחת מואץ", number=3, col_end=6 + MAX_YRS)
    R_ACCEL = R + 1

    sc(ws, R_ACCEL, 2,
       "שיעור פחת מואץ בשנה 1  ←  שנה ב'פרמטרי תמריץ'!F10",
       fill=PatternFill("solid", fgColor="FFE699"),
       font=Font(name="Arial", bold=True, size=11), align=A_R)
    sc(ws, R_ACCEL, 3, "% מה-CapEx", align=A_R)
    sc(ws, R_ACCEL, 4, "פרמטרי תמריץ", align=A_R)
    sc(ws, R_ACCEL, 5,
       "0% = ללא תמריץ (פחת סטנדרטי) | 100% = מחיקה מלאה בשנה 1",
       font=Font(name="Arial", italic=True, size=9, color="595959"), align=A_R)
    sc(ws, R_ACCEL, 6, f"={ACCEL_REF}",
       fill=F_INPUT,
       font=Font(name="Arial", bold=True, size=12, color="C00000"),
       fmt=FMT_PCT, align=A_C)

    R = R_ACCEL + 2

    # ── SECTION 4: DEPRECIATION SCHEDULES ──────────────────────────────────────
    section_hdr(ws, R, "לוחות פחת — השוואה", number=4, col_end=6 + MAX_YRS)
    year_header_row(ws, R + 1, MAX_YRS, yr0_label="שנה 0 (השקעה)")
    R_YH = R + 1
    R_SD  = R + 2   # standard depreciation
    R_ST  = R + 3   # standard tax shield
    R_AD  = R + 4   # accel depreciation
    R_AT  = R + 5   # accel tax shield

    labels4 = [
        (R_SD, "פחת שנתי — סטנדרטי",     F_NONE),
        (R_ST, "מגן מס — סטנדרטי",        F_RESULT),
        (R_AD, "פחת שנתי — מואץ",         F_ACCEL),
        (R_AT, "מגן מס — מואץ",           F_ACCEL),
    ]
    for rr, lbl, fill in labels4:
        sc(ws, rr, 2, lbl, fill=fill, font=FONT_N, align=A_R)
        sc(ws, rr, 3, "₪", align=A_R)
        sc(ws, rr, 4, "חישוב", align=A_R)
        sc(ws, rr, 6, 0, fill=fill, fmt=FMT_NIS, align=A_C)  # Year 0 = 0

    sc(ws, R_SD, 5, f"= CapEx × {tech['std_depr_pct']:.0%} | קו ישר | עד שנה {tech['std_depr_yrs']}", align=A_R)
    sc(ws, R_ST, 5, "= פחת × שיעור מס", align=A_R)
    sc(ws, R_AD, 5, "שנה 1 = CapEx × שיעור מואץ | יתרה מפוחתת בקו ישר", align=A_R)
    sc(ws, R_AT, 5, "= פחת מואץ × שיעור מס", align=A_R)

    capex_f   = f"$F${R_CAPEX}"
    std_r_f   = f"$F${R_SDPR}"
    tax_f     = f"$F${R_TAX}"
    disc_f    = f"$F${R_DISC}"
    accel_f   = f"$F${R_ACCEL}"
    svnis_f   = f"$F${R_SVNIS}"
    life_n    = tech['lifetime']
    std_yrs   = tech['std_depr_yrs']
    rem_yrs   = std_yrs - 1  # years 2..std_depr_yrs for remainder of accel

    for i in range(1, MAX_YRS + 1):
        col = 6 + i
        cl  = get_column_letter(col)

        # Standard depreciation: 0 after std_depr_yrs
        if i <= std_yrs:
            sd_val = f"=IF(ISNUMBER({capex_f}),{capex_f}*{std_r_f},0)"
        else:
            sd_val = "=0"
        sc(ws, R_SD, col, sd_val, fill=F_NONE, fmt=FMT_NIS, align=A_C)

        # Standard tax shield
        sc(ws, R_ST, col, f"={cl}{R_SD}*{tax_f}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)

        # Accelerated depreciation
        if i == 1:
            ad_val = f"=IF(ISNUMBER({capex_f}),{capex_f}*{accel_f},0)"
        elif 2 <= i <= std_yrs and rem_yrs > 0:
            ad_val = f"=IF(ISNUMBER({capex_f}),{capex_f}*(1-{accel_f})/{rem_yrs},0)"
        else:
            ad_val = "=0"
        sc(ws, R_AD, col, ad_val, fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

        # Accelerated tax shield
        sc(ws, R_AT, col, f"={cl}{R_AD}*{tax_f}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

    R = R_AT + 2

    # ── SECTION 5: CASH FLOW ANALYSIS ──────────────────────────────────────────
    section_hdr(ws, R, "ניתוח תזרים מזומנים", number=5, col_end=6 + MAX_YRS)
    year_header_row(ws, R + 1, MAX_YRS, yr0_label="שנה 0 (השקעה)")
    R_INV  = R + 2   # investment (year 0)
    R_ESV  = R + 3   # energy savings
    R_SN   = R + 4   # std net CF
    R_SD2  = R + 5   # std discounted CF
    R_SC   = R + 6   # std cumulative NPV
    R_AN   = R + 7   # accel net CF
    R_AD2  = R + 8   # accel discounted CF
    R_AC   = R + 9   # accel cumulative NPV

    row_labels5 = [
        (R_INV, "השקעה ראשונית (CapEx)",           F_NONE),
        (R_ESV, "חיסכון שנתי — אנרגיה",            F_NONE),
        (R_SN,  "תזרים נקי — ללא תמריץ",           F_NONE),
        (R_SD2, "תזרים מהוון — ללא תמריץ",          F_RESULT),
        (R_SC,  "NPV מצטבר — ללא תמריץ",           F_RESULT),
        (R_AN,  "תזרים נקי — עם תמריץ",            F_ACCEL),
        (R_AD2, "תזרים מהוון — עם תמריץ",           F_ACCEL),
        (R_AC,  "NPV מצטבר — עם תמריץ",            F_ACCEL),
    ]
    for rr, lbl, fill in row_labels5:
        sc(ws, rr, 2, lbl, fill=fill, font=FONT_N, align=A_R)
        sc(ws, rr, 3, "₪", align=A_R)
        sc(ws, rr, 4, "חישוב", align=A_R)

    # Year 0: investment = -CapEx; everything else = 0
    sc(ws, R_INV, 6, f"=IF(ISNUMBER({capex_f}),-{capex_f},\"PENDING\")", fmt=FMT_NIS, align=A_C)
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

        # Energy savings: apply for years 1..lifetime
        esv = f"=IF(ISNUMBER({svnis_f}),{svnis_f},0)" if i <= life_n else "=0"
        sc(ws, R_ESV, col, esv, fmt=FMT_NIS, align=A_C)

        # Std net = energy savings + std tax shield
        sc(ws, R_SN, col, f"={cl}{R_ESV}+{cl}{R_ST}", fmt=FMT_NIS, align=A_C)
        # Std discounted
        sc(ws, R_SD2, col, f"={cl}{R_SN}/(1+{disc_f})^{i}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)
        # Std cumulative
        sc(ws, R_SC, col, f"={pcl}{R_SC}+{cl}{R_SD2}",
           fill=F_RESULT, fmt=FMT_NIS, align=A_C)

        # Accel net = energy savings + accel tax shield
        sc(ws, R_AN, col, f"={cl}{R_ESV}+{cl}{R_AT}", fill=F_ACCEL, fmt=FMT_NIS, align=A_C)
        # Accel discounted
        sc(ws, R_AD2, col, f"={cl}{R_AN}/(1+{disc_f})^{i}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)
        # Accel cumulative
        sc(ws, R_AC, col, f"={pcl}{R_AC}+{cl}{R_AD2}",
           fill=F_ACCEL, fmt=FMT_NIS, align=A_C)

    R = R_AC + 2

    # ── SECTION 6: RESULTS ─────────────────────────────────────────────────────
    section_hdr(ws, R, "תוצאות", number=6, col_end=8)
    MAX_COL = get_column_letter(6 + MAX_YRS)

    R_NPV_S  = R + 1
    R_NPV_A  = R + 2
    R_DNPV   = R + 3
    # blank row R+4
    R_ROI_S  = R + 5
    R_ROI_A  = R + 6
    R_DROI   = R + 7
    # blank row R+8
    R_PBK_S  = R + 9
    R_PBK_A  = R + 10

    def result_row(ws, row, label, formula, fmt, fill=F_RESULT):
        sc(ws, row, 2, label,   fill=fill, font=Font(name="Arial", bold=True, size=10), align=A_R)
        sc(ws, row, 3, "ש\"ח" if "₪" in fmt else ("%" if "%" in fmt else "שנים"), align=A_R)
        sc(ws, row, 6, formula, fill=fill, fmt=fmt, align=A_C)

    result_row(ws, R_NPV_S, "NPV ללא תמריץ",
               f"=SUM(F{R_SD2}:{MAX_COL}{R_SD2})", FMT_NIS)
    result_row(ws, R_NPV_A, "NPV עם תמריץ",
               f"=SUM(F{R_AD2}:{MAX_COL}{R_AD2})", FMT_NIS, F_ACCEL)
    result_row(ws, R_DNPV,  "דלתא NPV — ערך התמריץ",
               f"=F{R_NPV_A}-F{R_NPV_S}", FMT_NIS, F_INPUT)

    result_row(ws, R_ROI_S, "ROI ללא תמריץ",
               f"=IF(ISNUMBER({capex_f}),(SUM(F{R_SD2}:{MAX_COL}{R_SD2})+{capex_f})/{capex_f},\"PENDING\")",
               FMT_PCT)
    result_row(ws, R_ROI_A, "ROI עם תמריץ",
               f"=IF(ISNUMBER({capex_f}),(SUM(F{R_AD2}:{MAX_COL}{R_AD2})+{capex_f})/{capex_f},\"PENDING\")",
               FMT_PCT, F_ACCEL)
    result_row(ws, R_DROI,  "שיפור ROI בזכות התמריץ",
               f"=IF(ISNUMBER(F{R_ROI_A}),F{R_ROI_A}-F{R_ROI_S},\"PENDING\")",
               FMT_PCT, F_INPUT)

    result_row(ws, R_PBK_S, "תקופת החזר — ללא תמריץ",
               f"=IF(ISNUMBER({svnis_f}),{capex_f}/{svnis_f},\"PENDING\")",
               FMT_YR)
    # payback with incentive: year1 benefits = energy savings + year1 accel tax shield
    result_row(ws, R_PBK_A, "תקופת החזר — עם תמריץ",
               f"=IF(ISNUMBER({svnis_f}),{capex_f}/({svnis_f}+G{R_AT}),\"PENDING\")",
               FMT_YR, F_ACCEL)

    sc(ws, R_PBK_A + 2, 2,
       "* תקופת ההחזר עם תמריץ משקפת את יתרון מגן המס בשנה הראשונה בלבד — לחישוב מדויק ראו NPV מצטבר",
       font=Font(name="Arial", italic=True, size=9, color="595959"), align=A_R)

    return ws, dict(
        npv_std=R_NPV_S, npv_acc=R_NPV_A, d_npv=R_DNPV,
        roi_std=R_ROI_S, roi_acc=R_ROI_A, d_roi=R_DROI,
        pbk_std=R_PBK_S, pbk_acc=R_PBK_A,
    )


# ─── SUMMARY SHEET ─────────────────────────────────────────────────────────────

def build_summary_sheet(wb, tech_results):
    ws = wb.create_sheet("סיכום")
    ws.sheet_view.rightToLeft = True

    widths = [4, 32, 18, 18, 18, 15, 15, 15, 14, 14]
    for i, w in enumerate(widths):
        ws.column_dimensions[get_column_letter(i + 1)].width = w

    color_legend(ws, row=1)

    ws.merge_cells('B8:J8')
    sc(ws, 8, 2, "סיכום — ניתוח פחת מואץ לפי טכנולוגיה",
       fill=F_HEADING, font=Font(name="Arial", bold=True, color="FFFFFF", size=13), align=A_R)

    sc(ws, 9, 2,
       f"* פרמטר המדיניות (שיעור פחת מואץ בשנה 1) = 'פרמטרי תמריץ'!F10 — שנה שם ותוצאות מתעדכנות אוטומטית",
       font=Font(name="Arial", italic=True, size=9, color="595959"), align=A_R)

    # Column headers
    hdrs = [
        (2, "טכנולוגיה"),
        (3, "NPV ללא תמריץ (₪)"),
        (4, "NPV עם תמריץ (₪)"),
        (5, "דלתא NPV (₪)"),
        (6, "ROI ללא תמריץ"),
        (7, "ROI עם תמריץ"),
        (8, "שיפור ROI"),
        (9, "תקופת החזר — ללא"),
        (10, "תקופת החזר — עם"),
    ]
    for col, lbl in hdrs:
        sc(ws, 10, col, lbl, fill=F_SUBHEAD, font=FONT_SH, align=A_C)

    for i, (tech, rmap) in enumerate(tech_results):
        row = 11 + i
        sn  = tech['sheet']
        sc(ws, row, 2, tech['name'], font=FONT_N, align=A_R)

        ref_data = [
            (3,  rmap['npv_std'], FMT_NIS, F_RESULT),
            (4,  rmap['npv_acc'], FMT_NIS, F_ACCEL),
            (5,  rmap['d_npv'],   FMT_NIS, F_INPUT),
            (6,  rmap['roi_std'], FMT_PCT, F_RESULT),
            (7,  rmap['roi_acc'], FMT_PCT, F_ACCEL),
            (9,  rmap['pbk_std'], FMT_YR,  F_RESULT),
            (10, rmap['pbk_acc'], FMT_YR,  F_ACCEL),
        ]
        for col, rr, fmt, fill in ref_data:
            sc(ws, row, col, f"='{sn}'!$F${rr}", fill=fill, fmt=fmt, align=A_C)

        # ROI improvement = col 7 - col 6
        sc(ws, row, 8, f"='{sn}'!$F${rmap['d_roi']}", fill=F_INPUT, fmt=FMT_PCT, align=A_C)

    # Note at bottom
    sc(ws, 16, 2,
       "** CapEx וצריכת אנרגיה שנתית עדיין ממתינים לנתוני רפי — לאחר הזנתם כל התוצאות יתעדכנו אוטומטית.",
       font=Font(name="Arial", italic=True, color="FF0000", size=9), align=A_R)


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    wb = openpyxl.Workbook()
    build_global_sheet(wb)
    build_policy_sheet(wb)

    tech_results = []
    for tech in TECHS:
        ws, rmap = build_tech_sheet(wb, tech)
        tech_results.append((tech, rmap))

    build_summary_sheet(wb, tech_results)

    out = "/home/user/shmags-2/projects/energy-program/tax_incentive_model.xlsx"
    wb.save(out)
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
