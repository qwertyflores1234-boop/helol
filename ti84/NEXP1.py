# NEXP1 notes - enter=next b=back q=quit
T="""== E.1 EXPONENTIAL FNS ==
f(x)=a*b^x (x in EXPONENT)
a = initial value = y-int
b = growth factor, b>0
b>1 GROWTH, 0<b<1 DECAY
3x^2 NOT exp (x is base)
4(1.3)^x: a=4, grow 30%
12(.75)^x: a=12, decay 25%
-- GRAPH FACTS --
Domain: all reals
Range: y>0 (if a>0)
HA: y=0, y-int (0,a)
points (0,a) and (1,a*b)
b>1 rises; x->-inf, y->0
0<b<1 falls; x->inf, y->0
(1/2)^x = 2^(-x): mirror
 of 2^x over the y-axis
both pass thru (0,1)
-- EVALUATE --
f(x)=3(2)^x: f(-2)=3/4
 neg exponent = 1/b^n
 f(0)=a always
-- FIND THE EQUATION --
y=b^x thru (3,125):
 b^3=125, b=125^(1/3)=5
 (EXP2PT: 0,1,3,125)
y-int (0,a) + pt (x,y):
 b=(y/a)^(1/x)
2 pts (x1,y1),(x2,y2):
 b=(y2/y1)^(1/(x2-x1))
 a=y1/b^x1
 ex (1,10),(3,40): b^2=4
  b=2, a=10/2=5
PROGRAMS: EXP2PT EXPINFO"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
