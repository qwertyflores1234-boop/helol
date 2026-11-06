# y=a*log_b(x-h)+k: domain, VA, x-int, inverse (E.3)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
def M(v):return '-'+F(v) if v>=0 else '+'+F(-v)
print('y=a*log_b(x-h)+k')
a=N('a=');b=N('b=');h=N('h=');k=N('k=')
print('domain x>'+F(h)+', VA x='+F(h))
print('range: all reals')
print('x-int x='+F(h+b**(-k/a)))
if h<0:print('y-int y='+F(a*log(-h)/log(b)+k))
print('increasing' if (b>1)==(a>0) else 'decreasing')
print('inverse: y=b^((x-k)/a)+h')
print(' ='+F(b)+'^((x'+M(k)+')/'+F(a)+')'+M(-h))
