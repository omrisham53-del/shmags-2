# Extension Prompt: Chiller Capacity Correction (300→120 RT) + Three New Chapter Sections

Paste into the Claude-in-Excel/Word extension. You have both the model (`מודל פחת מואץ`) and the tax chapter (`taxchapterdraft`, with the Results section already inserted through §5.4) open — this prompt touches both, in order: model first, then chapter.

---

## PART A — Model: correct chiller capacity to 120 RT

Omri checked the chiller capacity against the real grant-program data: the median installed capacity across actual funded projects is 117 RT, not the 300 RT currently in the model. Round to **120 RT**.

**Change:** in the assumptions sheet (`נתונים והנחות - כללי`), chiller capacity (`קיבולת מותקנת`, currently `F61 = 300`) → **120**.

Do NOT change anything else in that block — kW/ton efficiency rates (`F63`, `F64`), the ₪/ton CapEx rates (which are already rates, not absolute values), hours, lifespan, degradation all stay as they are. Capacity is the only input changing; everything downstream (consumption, CapEx, OPEX, cash flows, results) is formula-driven off it and will recompute automatically.

**Why the payback verdict won't change:** every dollar figure in the chiller block (CapEx and OPEX, baseline and efficient) scales linearly with capacity, since they're all `rate × capacity`. Payback period is a ratio between those figures, so capacity cancels out of it algebraically — the verdict is scale-invariant. Confirm this empirically after the change rather than assuming it, but it should hold.

### Expected values after the change (verify before proceeding to Part B)

| | at 300 RT (current) | at 120 RT (expected) |
|---|---|---|
| CapEx baseline | ₪1,068,600 | **₪427,440** |
| CapEx efficient | ₪1,255,800 | **₪502,320** |
| Consumption baseline | 697,500 kWh/yr | **279,000 kWh/yr** |
| Consumption efficient | 576,000 kWh/yr | **230,400 kWh/yr** |
| Payback B | 4.414 | **4.414 (unchanged)** |
| Payback C | 2.664 | **2.664 (unchanged)** |
| Verdict | incentive flips the decision | **unchanged** |
| Fiscal cost per unit (3%) | ₪18,174 | **₪7,270** |
| Economic value × 1,000 units | ₪293,956,865 | **₪117,582,746** |
| Fiscal cost × 1,000 units | ₪18,173,769 | **₪7,269,507** |

Everything above should scale by exactly **0.400** (= 120/300). If the payback numbers move at all, stop and investigate before touching the chapter — that would mean something else is capacity-dependent that shouldn't be.

**New program totals (all 3 technologies, heat pump and VSD unchanged):**

| | Was | Expect |
|---|---|---|
| Total economic value | ₪315,677,603 | **₪139,303,484** |
| Total fiscal cost | ₪21,126,029 | **₪10,221,767** |
| Electricity saved, 2026-2050 | 1,882,791,244 kWh | **~827,832,517 kWh** |
| CO2e avoided | 820,897 t | **~360,935 t** |
| External costs avoided | ₪226,762,267 | **~₪99,703,660** |
| Cost-effectiveness (additional techs only) | ~₪23.2/tCO2e | **~₪22.5/tCO2e** |

---

## PART B — Chapter: update the existing Results numbers

Everywhere "300" (RT) or these specific figures appear in the Results section already drafted, update to reflect Part A:

1. Opening paragraph of §5 and Table 2 (§5.1): "צ'ילרים (300 טון קירור)" → **"צ'ילרים (120 טון קירור)"**. Payback figures in Table 2 (4.41 / 2.66) stay the same.
2. Table 3 (§5.2, the 1,000-units table): chiller row — economic value 294.0 → **117.6** (millions ₪), fiscal cost 18.2 → **7.3** (millions ₪). Total row: 315.7 → **139.3**, 21.1 → **10.2**.
3. Energy/emissions paragraph (§5.3 in the current draft): "כ-1.88 מיליארד קוט״ש (כ-1,883 גיגה-ואט-שעה)" → **"כ-828 מיליון קוט״ש (כ-828 גיגה-ואט-שעה)"**; "כ-821 אלף טון CO2e" → **"כ-361 אלף טון"**; "כ-227 מיליון ₪" (external costs) → **"כ-100 מיליון ₪"**.
4. Cost-effectiveness paragraph (§5.4 in the current draft): "כ-19.0 מיליון ₪" (HP+chiller fiscal cost) → **"כ-8.1 מיליון ₪"**; "כ-821 אלף טון" → **"כ-361 אלף טון"**; "כ-23.2 ₪ לטון" → **"כ-22.5 ₪ לטון"**.

---

## PART C — Chapter: three new sections

Insert in this order, renumbering existing subsections so the flow reads: per-unit results → how the total is calculated → the total itself → the total's components (energy/emissions) → how that total is distributed over time → cost-effectiveness.

**New order:** 5.1 (existing, unchanged) → **5.2 [NEW below]** → 5.3 (existing table-3 section, renumbered from 5.2) → 5.4 (existing energy/emissions section, renumbered from 5.3) → **5.5 [NEW below]** → 5.6 (existing cost-effectiveness section, renumbered from 5.4).

### New §5.2 — שיטת חישוב התועלת הכוללת לתוכנית

Insert this text as a new subsection, right after §5.1's two paragraphs, before the existing 1,000-units table:

> התועלת הכוללת של ההטבה, המוצגת עבור 1,000 יחידות מכל טכנולוגיה, אינה סכום של תזרימי מזומנים שנתיים המהוונים מחדש לשנת הבסיס של התוכנית. במקום זאת, לכל טכנולוגיה מחושב תחילה הערך הכלכלי לאורך כל חיי היחידה הבודדת (חלופה ב' פחות חלופה א', מהוון בשיעור הפרטי של 6% ביחס לשנת ההתקנה של אותה יחידה) והעלות הפיסקלית ליחידה (חלופה ג' פחות חלופה ב', מהוונת בשיעור החברתי של 3%, גם היא ביחס לשנת ההתקנה). ערך זה מוכפל במספר היחידות המותקנות בכל שנה (1,000 חלקי אופק הניתוח של הטכנולוגיה), והתוצאה מסוכמת על פני כל שנות הפריסה שבתחום התוכנית (2026-2050).
>
> המשמעות המעשית היא שכל מחזור התקנה נמדד ביחס לשנת ההתקנה שלו עצמו, ולא ביחס לשנת הבסיס של התוכנית כולה. יחידה המותקנת ב-2035, לדוגמה, נמדדת בדיוק כמו יחידה המותקנת ב-2026 - שתיהן מייצגות את אותה החלטת השקעה בודדת, בנקודת הזמן שבה היא מתקבלת. גישה זו נכונה למדידת הערך שנוצר בכל מחזור התקנה בפני עצמו, אך אינה מהוונת את הערך שבין מחזורי ההתקנה השונים: תועלת שנוצרת ב-2045 אינה מהוונת בחזרה ל-2026 כדי לבטא שערכה, מנקודת המבט של היום, נמוך יותר מתועלת הנוצרת מיד. יש לבחון האם המתודולוגיה של פרק המענקים משתמשת באותה גישה, ולוודא התאמה בין הפרקים לפני גיבוש המסקנה הכלכלית הסופית של התוכנית הלאומית.

(This is the honest description of what the model actually does — a real open methodology question, not yet resolved. Do not soften it into sounding like a settled, fully-rigorous convention; it isn't yet.)

### New §5.5 — פרופיל החיסכון והפחתת הפליטות לאורך זמן

Insert after the (renumbered) energy/emissions section, before cost-effectiveness:

> מכיוון שהמודל מניח פריסה הדרגתית ואחידה של היחידות לאורך אופק הניתוח של כל טכנולוגיה, ולא התקנה חד-פעמית של כל 1,000 היחידות בבת אחת, פרופיל החיסכון השנתי באנרגיה ובפליטות עוקב אחר צורה אופיינית של עלייה, שיא וירידה.
>
> בשנים הראשונות לתוכנית מתווספת בכל שנה קבוצת התקנה חדשה על גבי הקבוצות הקיימות שעדיין פעילות, כך שהחיסכון המצטבר גדל משנה לשנה. השיא מתרחש כאשר כל מחזורי ההתקנה - מהראשון ועד האחרון - פעילים בו-זמנית, בשנת 2041 (תחילת התוכנית בתוספת אופק הניתוח של 15 שנה למשאבות חום ולצ'ילרים). מנקודה זו ואילך, מחזורי ההתקנה המוקדמים ביותר מגיעים לסוף חייהם התפעוליים ופורשים מהמלאי הפעיל, ומאחר שהמודל אינו מניח פריסה נוספת מעבר ל-1,000 היחידות המקוריות, אין מחזור התקנה חדש שמחליף אותם. כתוצאה מכך, החיסכון השנתי יורד בהדרגה מהשיא ב-2041 ועד תום אופק הטבלה ב-2050.
>
> ירידה זו היא תוצר של אופן ההצגה - סבב פריסה בודד של 1,000 יחידות - ואינה תחזית לכך שהחיסכון האמיתי מהתוכנית יידעך. תוכנית מתמשכת, שבה יחידות נוספות ממשיכות להיפרס גם לאחר תום מחזור ההתקנה הראשון, הייתה מציגה פרופיל שמתייצב סביב רמת השיא במקום לרדת ממנה. בנוסף, מחזורי ההתקנה המאוחרים ביותר (הפעילים סביב 2050) ממשיכים לחסוך אנרגיה מעבר לגבול הטבלה, וחלק זה נחתך על ידי גבול 2050 בלבד.
>
> טבלה 4 מציגה את החיסכון באנרגיה ואת הפחתת הפליטות בשתי שנות יעד נבחרות של התוכנית הלאומית.

Followed by a table, same styling as tables 2/3:

**טבלה 4 - חיסכון באנרגיה והפחתת פליטות בשנות יעד נבחרות**

| שנה | חיסכון אנרגטי שנתי (גיגה-ואט-שעה) | הפחתת פליטות שנתית (טון CO2e) |
|---|---|---|
| 2030 | 15.4 | 6,701 |
| 2035 | 35.0 | 15,268 |

(These reflect the post-Part-A numbers, chiller at 120 RT. If you build this table before completing Part A, the values will be wrong — do Part A first.)

---

## Final checklist

- [ ] Chiller capacity is 120 RT in the model, all downstream cells recomputed.
- [ ] No verdict changed (payback figures identical to before, only absolute ₪/kWh magnitudes moved).
- [ ] No `#REF!`/`#NAME?`/`#VALUE!` anywhere in either file after the edits.
- [ ] Every "300" / old-number instance in the chapter's Results section (opening paragraph, both tables, both prose paragraphs) is updated — search the whole §5 for "300" and "294" and "18.2" and "1.88" and "821" and "227" and "19.0" and "23.2" to catch anything missed.
- [ ] Section numbering in §5 is consistent after inserting the two new subsections (should read 5.1 through 5.6).
- [ ] New §5.2 and §5.5 use the same Calibri/RTL/heading-color styling as the rest of the chapter.
