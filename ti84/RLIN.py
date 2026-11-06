# Linear regression y=mx+b, r, R^2 (F.1)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
def L(m):
 while 1:
  try:return [float(eval(t.replace('^','**'),E)) for t in input(m).lower().split(',')]
  except:print('bad, retry')
def G():
 try:
  from ti_system import recall_list
  X=[float(v) for v in recall_list('1')];Y=[float(v) for v in recall_list('2')]
  if len(X)>1 and len(X)==len(Y):
   if input('Use L1,L2 ('+str(len(X))+' pts)? enter=yes n=no ')!='n':return X,Y
 except:pass
 print('type with commas: 1,2,3')
 return L('x list: '),L('y list: ')
def R(u,v):
 n=len(u);a=sum(u)/n;b=sum(v)/n
 sxx=sum((t-a)**2 for t in u);syy=sum((t-b)**2 for t in v)
 sxy=sum((u[i]-a)*(v[i]-b) for i in range(n))
 m=sxy/sxx
 return m,b-m*a,sxy/sqrt(sxx*syy)
X,Y=G()
m,b,r=R(X,Y)
print('y='+F(m)+'x+('+F(b)+')')
print('slope m='+F(m)+' int b='+F(b))
print('r='+F(r)+' R^2='+F(r*r))
w=abs(r)
s='strong' if w>=.8 else 'moderate' if w>=.5 else 'weak'
print('no correlation' if w<.1 else s+(' positive' if r>0 else ' negative'))
f=lambda x:m*x+b
I=lambda t:(t-b)/m
while 1:
 c=input('1:y(x) 2:x(y) 0:quit ')
 try:
  if c=='1':x=N('x=');print('y='+F(f(x)))
  if c=='2':t=N('y=');print('x='+F(I(t)))
 except:print('undefined')
 if c=='0':break
