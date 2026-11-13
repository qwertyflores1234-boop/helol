# ANNUITY G.2: FV/PV, ordinary/due
from math import *
def fv(R,i,n,d):return R*((1+i)**n-1)/i*(1+i)**d
def pv(R,i,n,d):return R*(1-(1+i)**-n)/i*(1+i)**d
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
def N(p):
 while 1:
  try:return float(input(p))
  except:print('Bad entry, retry')
def Y(v):return '$'+'%.2f'%v
def A(fut,d):
 V='S' if fut else 'P'
 s=input('Solve 1'+V+' 2R 3n 4r ?')
 if s<'1' or s>'4' or len(s)!=1:return
 if s!='4':r=N('r %=')/100
 m=N('m per yr=')
 if s!='1':v=N(V+'=')
 if s!='2':R=N('R pmt=')
 if s!='3':n=m*N('t yrs=')
 if s=='4':
  r=ann_r(v,R,m,n,d,fut)
  if r is None:print('no rate 0-100%');return
  print('r='+'%.4f'%(r*100)+'%')
 i=r/m;f=fv if fut else pv
 if s=='1':v=f(R,i,n,d);print(V+'='+Y(v))
 if s=='2':R=v/f(1,i,n,d);print('R='+Y(R))
 if s=='3':
  n=ann_n(v,R,i,d,fut)
  if n is None:print('never paid off');return
  print('n='+'%.4f'%n)
  if abs(n-round(n))>1e-3:print('round up: '+str(int(ceil(n)))+' pmts')
  print('t='+'%.2f'%(n/m)+' yrs')
 print('total pmts='+Y(n*R))
 print('interest='+Y(v-n*R if fut else n*R-v))
def main():
 while 1:
  print('1 FV ord   2 FV due');print('3 PV ord   4 PV due');print('0 Quit')
  c=input('?')
  if c=='0':break
  if c in('1','2','3','4'):
   k=int(c)
   try:A(k<3,1-k%2)
   except:print('Math error-check')
   input('Press Enter')
try:INTEREST_TEST
except NameError:main()
