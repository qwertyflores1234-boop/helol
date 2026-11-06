# NEQ notes - enter=next b=back q=quit
T="""== E.4 SOLVING ==
EXPONENTIAL EQUATION:
1 isolate b^( )
 (undo +,- then *,/)
2 rewrite b^u=v as
 u=log_b v (or ln both)
3 solve for x
4e^(.3x)+2=18:
 e^(.3x)=4, .3x=ln4
 x=4.621
SAME BASE: 5^(2x-1)=125
 125=5^3 so 2x-1=3, x=2
7(1.4)^x=30: 1.4^x=30/7
 x=ln(30/7)/ln1.4=4.325
-- ONE LOG --
1 isolate log_b( )
2 log_b u=v -> u=b^v
3 solve, CHECK domain
log_3(x-2)=4: x-2=81
2lnx-3=7: lnx=5, x=e^5
-- MANY LOGS --
1 condense into ONE log
2 log A=log B -> A=B
 else log_b A=v -> A=b^v
3 solve (often quadratic)
4 CHECK each answer: every
 log input must be >0
 fails = EXTRANEOUS
log2x+log2(x-2)=3
 x(x-2)=8 -> x=4 (not -2)
ln(x+3)-ln(x-1)=ln2
 (x+3)/(x-1)=2 -> x=5
-- WORD PROBLEM --
2000(1.06)^t=3500
 t=ln(1.75)/ln1.06=9.60
 whole years -> 10
PROGRAMS: EXPSOLVE
 LOGSOLVE EQSOLVE"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
