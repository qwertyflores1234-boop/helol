# NNONLIN notes - enter=next b=back q=quit
T="""== F.2 NONLINEAR REG ==
PICK THE MODEL:
same AMOUNT each step
 -> LINEAR (+8 per x)
same PERCENT each step
 -> EXPONENTIAL (+8%)
rises then falls (U or
 upside-down U)
 -> QUADRATIC
rises fast then slows
 -> LOG y=a+b*ln x
-- QUADRATIC/POLY --
y=ax^2+bx+c
Excel: Polynomial Order 2
 (Order 3 = cubic)
line misses curve: the
 y differences change
higher order = higher R^2
 but OVERFITS, bad
 predictions outside data
-- EXPONENTIAL --
Excel: Exponential, shows
 y=a*e^(kx), needs y>0
to y=a*b^x: b=e^k
to e form: k=ln(b)
rate: b-1 grow, 1-b decay
12e^(.08x)=12(1.0833)^x
 8.33% growth
90(.7)^x=90e^(-.3567x)
 30% decay
-- LOGARITHMIC --
Excel: Logarithmic
y=c*ln(x)+b, needs x>0
type e^n in Excel: =EXP(n)
-- TIPS --
keep 4-6 digits; rounding
 grows in exp/powers
Excel: Format Trendline
 Label>Number>decimals
highest R^2 fits best
PROGRAMS: RPOLY REXP RLOG
 RPOW CONVBK RLIN"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
