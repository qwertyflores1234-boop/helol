# y=a*b^x through 2 points (E.1/E.2)
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
print('y=a*b^x thru 2 points')
print('start value? use x1=0')
p=N('x1=');q=N('y1=');r=N('x2=');s=N('y2=')
b=(s/q)**(1/(r-p))
print('b=(y2/y1)^(1/(x2-x1))')
print(' =('+F(s)+'/'+F(q)+')^(1/'+F(r-p)+')='+F(b))
print('a=y1/b^x1='+F(q/b**p))
S(q/b**p,b)
