# y=a*b^x from start + rate/doubling/half-life (E.2)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
def S(a,b):
 k=log(b)
 print('y='+F(a)+'*'+F(b)+'^x')
 print('y='+F(a)+'e^('+F(k)+'x)')
 if b>1:print('grow '+F(100*b-100)+'%/x');print('double time '+F(log(2)/k))
 if b<1:print('decay '+F(100-100*b)+'%/x');print('half-life '+F(log(.5)/k))
 while 1:
  c=input('1:y(x) 2:x(y) 0:quit ')
  try:
   if c=='1':x=N('x=');print('y='+F(a*b**x))
   if c=='2':t=N('y=');print('x='+F(log(t/a)/k))
  except:print('no solution')
  if c=='0':break
print('y=a*b^x from start+rate')
a=N('start a=')
print('1:grows r%  2:decays r%')
print('3:x factor (2=dbl,.5=half)')
c=input('? ')
if c=='3':m=N('factor=')
else:
 r=N('rate %=')/100
 m=1-r if c=='2' else 1+r
T=N('every how many x? ')
b=m**(1/T)
print('b='+F(m)+'^(1/'+F(T)+')='+F(b))
S(a,b)
