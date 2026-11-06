# log_b(x)=y <=> b^y=x, solve for any one (E.3)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
print('log_b(x)=y <=> b^y=x')
print('leave unknown blank')
V=[]
for m in ('b=','x=','y='):
 s=input(m)
 V.append(None if s=='' else float(eval(s.replace('^','**'),E)))
b,x,y=V
if b is None:b=x**(1/y)
elif x is None:x=b**y
else:y=log(x)/log(b)
print('log_'+F(b)+'('+F(x)+')='+F(y))
print(F(b)+'^'+F(y)+'='+F(x))
