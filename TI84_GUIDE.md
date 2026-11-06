# TI-84 Plus CE Python: MATH 1311 Programs (E.1 to F.2)

All programs are in the `ti84/` folder. Each one is small (under 2 KB) so it fits in the
calculator's Python memory. Bigger programs give `MemoryError`.

## Install
1. In TI Connect CE → Calculator Explorer, delete the old **EXPFN, LOGEQ, REGRESS, SOLVER** if they're still there.
2. Close the Python App on the calculator (2nd + mode).
3. Drag all `.py` files from `ti84/` into Calculator Explorer.
4. In the Send box, set **Location = RAM**. Archived files did not show up in the Python App.
5. Unplug, then open **apps → Python**. Pick a program and press **[y=] Run**.

## Which program to use

### E.1 / E.2: Exponential functions
| Program | Problem type |
|---|---|
| **EXP2PT** | Exponential through 2 points. For "starts at a, after x it's y", use x1=0, y1=a. |
| **EXPRATE** | Starts at a and grows/decays r%, or doubles/halves (factor 2 or .5) every T |
| **INTEREST** | A=P(1+r/n)^(nt). Use n=0 for continuous (Pe^(rt)). |
| **CONVBK** | Convert a·b^x ⇄ a·e^(kx) (k=ln b, b=e^k) |

EXP2PT and EXPRATE show both forms, the growth/decay %, and the doubling time or half-life.
Then they let you find **y at x** or **x for y**.

### E.3 / E.4: Logs and equations
| Program | Problem type |
|---|---|
| **LOGB** | log_b(x)=y ⇄ b^y=x. Leave the unknown blank. It also evaluates logs. |
| **EXPSOLVE** | a·b^(cx+d)+f=k, with steps |
| **LOGSOLVE** | a·log_b(cx+d)+f=k, with steps |
| **EQSOLVE** | **Any** equation (multiple logs, different bases...). Invalid answers are rejected automatically. |
| **LOGINFO** | y=a·log_b(x−h)+k: domain, VA, x-int, inc/dec, inverse |
| **EXPINFO** | y=a·b^(x−h)+k: range, HA, intercepts, inverse |
| **CONDENSE** | c1·log(A)+c2·log(B)+… → one log |

In EQSOLVE type `ln(x)`, `log(x)` (base 10), `logb(3,x)` (log base 3), `e^x`, `2x`.
Give a search range (try −20 to 20; use 0 to 50 for logs).

### F.1 / F.2: Regression (same results as Excel trendlines)
Put x's in **L1** and y's in **L2** (stat → Edit). The programs ask "Use L1,L2?", so just press enter.
Or press `n` and type the lists with commas.

| Program | Fit |
|---|---|
| **RLIN** | Linear y=mx+b, r, R², correlation strength/direction |
| **RPOLY** | Quadratic (degree 2) or polynomial (3 to 6), R² |
| **REXP** | Exponential y=ae^(kx) **and** y=a·b^x, R² |
| **RLOG** | Logarithmic y=c·ln(x)+b, R² |
| **RPOW** | Power y=a·x^p, R² |

All of them except RPOLY can predict **y at x** and **x for y**. RPOLY only does y at x;
for x from y, use EQSOLVE with the polynomial.

## Typing tips
- Letters: [alpha]. Use the [^] key for powers. Negative numbers: (−) or minus both work.
- `ln(` = natural log, `log(` = base 10. If the [ln] key pastes `log(`, type `ln` with letters.
- For base e, type `e` when asked for b.
- Press [on] to stop a frozen program.
