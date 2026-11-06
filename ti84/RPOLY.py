# Quadratic/polynomial regression like Excel (F.2)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%(0 if abs(v)<1e-9 else v)
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
d=int(N('degree (2=quad)='))
n=len(X);mx=sum(X)/n;s=max(abs(t-mx) for t in X)
T=[(t-mx)/s for t in X]
A=[[sum(t**(i+j) for t in T) for j in range(d+1)]+[sum(Y[k]*T[k]**i for k in range(n))] for i in range(d+1)]
for i in range(d+1):
 for j in range(i+1,d+1):
  z=A[j][i]/A[i][i]
  for k in range(i,d+2):A[j][k]-=z*A[i][k]
C=[0]*(d+1)
for i in range(d,-1,-1):C[i]=(A[i][d+1]-sum(A[i][k]*C[k] for k in range(i+1,d+1)))/A[i][i]
p=[C[d]]
for i in range(d-1,-1,-1):
 q=[0]*(len(p)+1)
 for j in range(len(p)):q[j+1]+=p[j]/s;q[j]-=p[j]*mx/s
 q[0]+=C[i];p=q
def f(x):
 v=0
 for c in reversed(p):v=v*x+c
 return v
for i in range(d,-1,-1):print('x^'+str(i)+': '+F(p[i]))
my=sum(Y)/n
print('R^2='+F(1-sum((Y[i]-f(X[i]))**2 for i in range(n))/sum((t-my)**2 for t in Y)))
while 1:
 c=input('1:y(x) 0:quit ')
 if c=='1':x=N('x=');print('y='+F(f(x)))
 if c=='0':break
