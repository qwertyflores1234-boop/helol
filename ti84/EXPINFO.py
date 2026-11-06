# y=a*b^(x-h)+k: range, HA, intercepts, inverse (E.3)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
def M(v):return '' if v==0 else '-'+F(v) if v>0 else '+'+F(-v)
print('y=a*b^(x-h)+k')
a=N('a=');b=N('b=');h=N('h=');k=N('k=')
print('domain: all reals')
print('range y'+('>' if a>0 else '<')+F(k)+', HA y='+F(k))
print('y-int y='+F(a*b**(-h)+k))
v=-k/a
print('x-int x='+F(h+log(v)/log(b)) if v>0 else 'no x-int')
print('inverse: y=log_b((x-k)/a)+h')
print(' =log_'+F(b)+'((x'+M(k)+')/'+F(a)+')'+M(-h))
