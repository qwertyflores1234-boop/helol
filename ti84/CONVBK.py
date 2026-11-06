# Convert y=a*b^x <-> y=a*e^(kx)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
print('1:a*b^x -> a*e^(kx)')
print('2:a*e^(kx) -> a*b^x')
c=input('? ');a=N('a=')
if c=='2':k=N('k=');print('b=e^k='+F(exp(k)));print('y='+F(a)+'*'+F(exp(k))+'^x')
else:b=N('b=');print('k=ln(b)='+F(log(b)));print('y='+F(a)+'e^('+F(log(b))+'x)')
