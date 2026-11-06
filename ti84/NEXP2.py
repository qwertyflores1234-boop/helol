# NEXP2 notes - enter=next b=back q=quit
T="""== E.2 APPLICATIONS ==
t=time, a=start amount
grow r%:  b=1+r
decay r%: b=1-r
 (r decimal: 15%=.15)
rate from b: (b-1)*100%
b=.85 means keeps 85%
 each period, loses 15%
"a at start, Y after T":
 b=(Y/a)^(1/T)
 160g->20g in 6h:
 b=(20/160)^(1/6)=.7071
 loses 29.29%/hour
-- DOUBLE / HALF --
doubles every T:
 y=a*2^(t/T)
half-life T:
 y=a*(1/2)^(t/T)
triples every T: a*3^(t/T)
why t/T? 500*2^t doubles
 every 1 hr, not every 3
as a*b^t: b=2^(1/T)
double time = ln2/ln b
half-life = ln(.5)/ln b
-- WHEN DOES IT HIT Y --
a*b^t=Y
 t=ln(Y/a)/ln(b)
"first whole year": round
 t UP, check value there
-- INTEREST --
A=P(1+r/n)^(nt)
 n: 1 yr, 4 quarter,
 12 month, 365 day
continuous: A=P*e^(rt)
PROGRAMS: EXP2PT EXPRATE
 INTEREST CONVBK"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
