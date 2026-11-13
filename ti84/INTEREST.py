# INTEREST G.1: compound, continuous, APY, simple
from math import *
def gf(r,m,t):return exp(r*t) if m==0 else (1+r/m)**(m*t)
def lump_t(P,A,r,m):return log(A/P)/r if m==0 else log(A/P)/(m*log(1+r/m))
def lump_r(P,A,m,t):return log(A/P)/t if m==0 else m*((A/P)**(1/(m*t))-1)
def apy(r,m):return exp(r)-1 if m==0 else (1+r/m)**m-1
def simple(P,r,t):return P*r*t,P*(1+r*t)
def N(p):
 while 1:
  try:return float(input(p))
  except:print('Bad entry, retry')
def PC():return N('r %=')/100
def Y(v):return '$'+'%.2f'%v
def PT(v):return '%.4f'%(v*100)+'%'
def L(c):
 s=input('Solve 1A 2P 3t 4r ?')
 if s<'1' or s>'4' or len(s)!=1:return
 if s!='1':A=N('A=')
 if s!='2':P=N('P=')
 if s!='4':r=PC()
 m=0 if c else N('m per yr=')
 if s!='3':t=N('t yrs=')
 if s=='1':A=P*gf(r,m,t)
 if s=='2':P=A/gf(r,m,t)
 if s=='3':print('t='+'%.2f'%lump_t(P,A,r,m)+' yrs')
 if s=='4':print('r='+PT(lump_r(P,A,m,t)))
 print('A='+Y(A)+' P='+Y(P))
 print('interest='+Y(A-P))
def AP():
 B=[]
 for k in range(int(N('offers 1 or 2='))):
  B.append(apy(PC(),N('m/yr 0=cont=')));print('APY='+PT(B[-1]))
 if len(B)>1:print('offer '+('1' if B[0]>=B[1] else '2')+' higher APY');print('(better for saving)')
def S():
 s=input('Solve 1I/A 2P 3r 4t ?')
 k='1' if s=='1' else input('know 1 I or 2 A?')
 if s!='2':P=N('P=')
 if s!='1':
  if k=='2':A=N('A=')
  else:I=N('I=')
 if s!='3':r=PC()
 if s!='4':t=N('t yrs=')
 if s=='2':P=A/(1+r*t) if k=='2' else I/(r*t)
 if k=='2':I=A-P
 if s=='3':r=I/(P*t);print('r='+PT(r))
 if s=='4':t=I/(P*r);print('t='+'%.2f'%t+' yrs')
 I,A=simple(P,r,t)
 print('P='+Y(P)+' I='+Y(I));print('A='+Y(A))
def main():
 while 1:
  print('1 Compound 2 Continuous');print('3 APY  4 Simple  0 Quit');print('annuities: ANNUITY')
  c=input('?')
  if c=='0':break
  try:
   if c=='1':L(0)
   if c=='2':L(1)
   if c=='3':AP()
   if c=='4':S()
  except:print('Math error-check')
  input('Press Enter')
try:INTEREST_TEST
except NameError:main()
