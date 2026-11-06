# NINDEX - which program to use
T="""== WHICH PROGRAM? ==
2 points / start+point
 -> EXP2PT
start + rate%/double/half
 -> EXPRATE
interest P(1+r/n)^nt
 -> INTEREST
a*b^x <-> a*e^(kx)
 -> CONVBK
exp graph/inverse
 a*b^(x-h)+k -> EXPINFO
log graph/inverse
 a*log_b(x-h)+k -> LOGINFO
log<->exp form, log value
 -> LOGB (blank unknown)
combine logs -> CONDENSE
a*b^(cx+d)+f=k -> EXPSOLVE
a*log_b(cx+d)+f=k
 -> LOGSOLVE
anything else / many logs
 -> EQSOLVE: logb(2,x)
 ln( ) log( ) e^x 2x ok
 logs: search 0 to 50
regression (L1=x, L2=y):
 RLIN linear, r, R^2
 RPOLY quad=degree 2
 REXP exponential
 RLOG logarithmic
 RPOW power
NOTES: NEXP1 NEXP2 NLOG1
 NLOG2 NEQ NLIN NNONLIN
b=e: type e
negatives: (-) key"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
