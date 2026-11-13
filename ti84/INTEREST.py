# INTEREST - G.1/G.2 interest and annuities
from math import *
# ---- math (tested by tests/test_interest.py) ----
def gf(r,m,t):
 return exp(r*t) if m==0 else (1+r/m)**(m*t)
def lump_t(P,A,r,m):
 return log(A/P)/r if m==0 else log(A/P)/(m*log(1+r/m))
def lump_r(P,A,m,t):
 return log(A/P)/t if m==0 else m*((A/P)**(1/(m*t))-1)
def apy(r,m):
 return exp(r)-1 if m==0 else (1+r/m)**m-1
def fv(R,i,n,d):
 return R*((1+i)**n-1)/i*(1+i)**d
def pv(R,i,n,d):
 return R*(1-(1+i)**-n)/i*(1+i)**d
def ann_n(V,R,i,d,fut):
 x=V*i/(R*(1+i)**d)
 if fut:return log(1+x)/log(1+i)
 if x>=1:return None
 return -log(1-x)/log(1+i)
def ann_r(V,R,m,n,d,fut):
 f=fv if fut else pv
 g=lambda r:f(R,r/m,n,d)-V
 a=1e-6;b=1.0;ga=g(a)
 if (ga<0)==(g(b)<0):return None
 for k in range(100):
  c=(a+b)/2;gc=g(c)
  if (gc<0)==(ga<0):a,ga=c,gc
  else:b=c
  if b-a<1e-10:break
 return (a+b)/2
def simple(P,r,t):
 return P*r*t,P*(1+r*t)
# ---- input/output ----
def N(p):
 while 1:
  try:return float(input(p))
  except:print('Bad entry, retry')
def PC(p):return N(p+' %=')/100
def MM(c):
 if c:return 0
 return N('m per yr=')
def Y(v):return '$'+'%.2f'%v
def PT(v):return '%.4f'%(v*100)+'%'
def W():input('Press Enter')
def ASK(o):
 print('Solve for?')
 print(o)
 return input('?').strip()
def SN(n,m):
 print('n='+'%.4f'%n)
 if abs(n-round(n))>1e-3:print('round up: '+str(int(ceil(n)))+' pmts')
 print('t='+'%.2f'%(n/m)+' yrs')
def lump(c):
 s=ASK('1 A  2 P  3 t  4 r')
 if s=='1':
  P=N('P=');r=PC('r');m=MM(c);t=N('t yrs=');A=P*gf(r,m,t)
 elif s=='2':
  A=N('A=');r=PC('r');m=MM(c);t=N('t yrs=');P=A/gf(r,m,t)
 elif s=='3':
  P=N('P=');A=N('A=');r=PC('r');m=MM(c)
  print('t='+'%.2f'%lump_t(P,A,r,m)+' yrs')
 elif s=='4':
  P=N('P=');A=N('A=');m=MM(c);t=N('t yrs=')
  print('r='+PT(lump_r(P,A,m,t)))
 else:return
 print('A='+Y(A)+' P='+Y(P))
 print('interest='+Y(A-P))
def apym():
 B=[]
 for k in range(int(N('offers (1/2)='))):
  r=PC('r');m=N('m/yr (0=cont)=')
  B.append(apy(r,m));print('APY='+PT(B[-1]))
 if len(B)==2:
  print('offer '+('1' if B[0]>=B[1] else '2')+' has higher APY')
  print('(better for saving)')
def ann(fut,d):
 V='S' if fut else 'P'
 s=ASK('1 '+V+'  2 R  3 n  4 r')
 if s not in '1234' or s=='':return
 if s!='4':r=PC('r')
 m=N('m per yr=')
 if s!='1':v=N(V+'=')
 if s!='2':R=N('R pmt=')
 if s!='3':n=m*N('t yrs=')
 if s=='4':
  r=ann_r(v,R,m,n,d,fut)
  if r is None:print('no rate 0-100%');return
  print('r='+PT(r))
 i=r/m
 f=fv if fut else pv
 if s=='1':v=f(R,i,n,d);print(V+'='+Y(v))
 if s=='2':R=v/f(1,i,n,d);print('R='+Y(R))
 if s=='3':
  n=ann_n(v,R,i,d,fut)
  if n is None:print('never paid off');return
  SN(n,m)
 print('total pmts='+Y(n*R))
 print('interest='+Y(v-n*R if fut else n*R-v))
def simp():
 s=ASK('1 I/A  2 P  3 r  4 t')
 if s=='1':
  P=N('P=');r=PC('r');t=N('t yrs=')
 else:
  k=input('know 1 I or 2 A?')
  if s!='2':P=N('P=')
  I=N('I=') if k!='2' else 0
  if k=='2':A=N('A=')
  if s!='3':r=PC('r')
  if s!='4':t=N('t yrs=')
  if s=='2':P=I/(r*t) if k!='2' else A/(1+r*t)
  if k=='2':I=A-P
  if s=='3':r=I/(P*t);print('r='+PT(r))
  if s=='4':t=I/(P*r);print('t='+'%.2f'%t+' yrs')
 I,A=simple(P,r,t)
 print('P='+Y(P)+' I='+Y(I))
 print('A='+Y(A))
def main():
 while 1:
  print('1 Compound 2 Continuous')
  print('3 APY/Effective')
  print('4 FV ord   5 FV due')
  print('6 PV ord   7 PV due')
  print('8 Simple   0 Quit')
  c=input('?').strip()
  if c=='0':break
  try:
   if c=='1':lump(0)
   elif c=='2':lump(1)
   elif c=='3':apym()
   elif c in('4','5','6','7'):k=int(c);ann(k<6,k%2)
   elif c=='8':simp()
   else:continue
  except:print('Math error-check')
  W()
try:INTEREST_TEST
except NameError:main()
