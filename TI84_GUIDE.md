# TI-84 Plus CE Python: MATH 1311 Programs (E.1 to F.2)

| Program | Sections | Use it for |
|---|---|---|
| `EXPFN.py` | E.1, E.2 | Building `y = a*b^x` from points or word problems, growth/decay, interest |
| `LOGEQ.py` | E.3, E.4 | Logs, log/exp form, solving log and exponential equations, inverses |
| `REGRESS.py` | F.1, F.2 | Linear, quadratic, polynomial, exponential, log and power trendlines (same as Excel) |
| `SOLVER.py` | any | General f(x) tool: roots, derivative, integral, table |

## Install
1. Install **TI Connect CE** on a computer and plug in the calculator.
2. Drag the `.py` files onto the calculator (they become Python AppVars).
3. On the calculator: **[prgm] → Python App → pick the file → Run**.

## Typing tips
- `^` works for powers, and `2x` means `2*x`.
- `ln(` = natural log, `log(` = base 10, `logb(b,x)` = log base b, `e^x` or `exp(x)`.
- Type letters with **[alpha]**. If your **[ln]** key pastes `log(`, type `ln(` by hand,
  because in these programs `log` means base 10.
- Rates are entered as percents (`5` means 5%).
- Press **[enter]** to move past each result screen.

## EXPFN: Exponential (E.1 / E.2)
| Menu | Problem type | Example → answer |
|---|---|---|
| 1 | Through two points | (1,6),(3,54) → `y=2*3^x` |
| 2 | Initial value + one later point | starts 200, 350 after 4 yrs → `b=(350/200)^(1/4)` |
| 3 | Initial + grows/decays r% | 500, decays 8%/yr → `y=500*0.92^x` |
| 4 | Initial + doubles/halves/triples every T | 100 g, half-life 5730 → `b=0.5^(1/5730)` |
| 5/6 | You already have a, b (or a, k) | convert between `a*b^x` and `a*e^(kx)` |
| 7 | Compound/continuous interest | $1000, 5%, monthly → APY 5.116%, doubles in 13.89 yrs |
| 8 | Fact sheet | |

After any model is made you can: **find y at x**, **find x for a y** (when it reaches a value),
**see info** (growth/decay %, k, doubling time or half-life, asymptote, domain/range),
**average rate of change** between two x's, and **time to multiply by a factor**.

## LOGEQ: Logs and equations (E.3 / E.4)
| Menu | Does | Example → answer |
|---|---|---|
| 1 | log_b(x) by change of base | log₂32 = 5 |
| 2 | Log ⇄ exponential form (leave the unknown blank) | log₃x = 4 → x = 81 |
| 3 | `a*b^(cx+d)+f=k` with steps | 5·2^(3x−1)+4=104 → x = 1.77398 |
| 4 | `a*log_b(cx+d)+f=k` with steps | 2log₃(x+2)+5=17 → x = 727 |
| 5 | **Any** equation, numeric. Also rejects answers outside the domain | log(x)+log(x−3)=1 → x=5 (−2 rejected); 2^(x+1)=3^(x−2) → 7.12853 |
| 6 | Log function `a*log_b(x-h)+k`: domain, VA, intercepts, inc/dec, inverse | |
| 7 | Exp function `a*b^(x-h)+k`: range, HA, intercepts, inverse | |
| 8 | Condense logs (power/product/quotient rules) | 2log x + log y − 3log(z+1) → log((x)²(y)/(z+1)³) |
| 9 | Fact sheet (all log properties) | |

## REGRESS: Regression (F.1 / F.2)
1. **1** to enter data (`1,2,3,4` for x's, then the y's), or **2** to load from lists L1/L2.
2. Pick a fit: **4** linear, **5** quadratic, **6** polynomial (degree 2 to 6), **7** exponential,
   **8** logarithmic, **9** power.
   - Linear shows slope, intercept, **r**, **R²** and the correlation (strong/moderate/weak, positive/negative).
   - Exponential shows Excel's `y=ae^(kx)` **and** the `y=a*b^x` form (b = e^k).
   - Exp/log/power R² are computed the same way Excel does, so numbers match Excel trendlines.
3. **10** compares R² for every fit type.
4. **11** predicts using the last fit: y at an x, or which x gives a y.
5. **12** converts `a*b^x ⇄ a*e^(kx)` (k = ln b, b = e^k).
6. **13** plots the data and the trendline. **14** shows the fact sheet, including the Excel steps.

The regression programs were checked against numpy. The E.1 to E.4 examples above were checked by hand.
