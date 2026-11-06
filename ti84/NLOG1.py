# NLOG1 notes - enter=next b=back q=quit
T="""== E.3 LOGARITHMS ==
log_b(x)=y MEANS b^y=x
"base ^ answer = inside"
ln x = log base e
log x = log base 10
e = 2.71828...
-- TO EXPONENTIAL FORM --
log_2 32=5    -> 2^5=32
log(.001)=-3  -> 10^-3=.001
ln 7=x        -> e^x=7
-- TO LOG FORM --
3^4=81   -> log_3 81=4
5^-2=1/25 -> log_5(1/25)=-2
e^x=12   -> x=ln 12=2.4849
-- EVALUATE, NO CALC --
ask: b to WHAT power = x?
log_2 64=6 (2^6=64)
log_3(1/27)=-3 (3^-3)
log_b 1=0     log_b b=1
log_b(b^n)=n  ln(e^5)=5
b^(log_b x)=x
log(sqrt 10)=1/2
 sqrt x = x^(1/2)
 1/x^n = x^(-n)
PROGRAM: LOGB (blank =
 the unknown)"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
