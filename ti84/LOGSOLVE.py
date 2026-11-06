# Solve a*log_b(cx+d)+f=k with steps (E.4)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
print('a*log_b(cx+d)+f=k (b=e ok)')
a=N('a=');b=N('b=');c=N('c=');d=N('d=');f=N('f=');k=N('k=')
v=(k-f)/a
print('log_b(cx+d)='+F(v))
u=b**v
print('cx+d=b^'+F(v)+'='+F(u))
print('x=('+F(u)+'-d)/c='+F((u-d)/c))
