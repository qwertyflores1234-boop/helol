# NLOG2 notes - enter=next b=back q=quit
T="""== E.3 LOG GRAPH ==
y=log_b(x):
Domain x>0 (positives)
Range: all reals
VA: x=0
x-int (1,0)
pts (1,0),(b,1),(1/b,-1)
b>1 increasing
0<b<1 decreasing
INVERSE of y=b^x
 log_2 x <-> 2^x
 graphs mirror over y=x
 (swap x and y coords)
y=a*log_b(x-h)+k:
 domain x>h, VA x=h
 x+4 means h=-4
-- PROPERTIES --
PRODUCT log(xy)=logx+logy
QUOTIENT log(x/y)=logx-logy
POWER log(x^p)=p*logx
log(x+y) is NOT logx+logy
EXPAND ln(x^3*sqrt(y)/z^2)
 =3lnx+(1/2)lny-2lnz
CONDENSE 2logx+logy-3logz
 coef -> power,
 + multiply, - divide
 =log(x^2*y/z^3)
-- CHANGE OF BASE --
log_b x = ln x / ln b
log_4 11=ln11/ln4=1.7297
PROGRAMS: LOGINFO EXPINFO
 CONDENSE LOGB"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
