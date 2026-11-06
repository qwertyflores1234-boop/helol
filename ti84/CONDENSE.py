# c1*log(A)+c2*log(B)+... -> one log (E.4)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
print('c1*log(A)+c2*log(B)...')
n=int(N('# terms='));T=[];B=[]
for i in range(n):
 c=N('coef=');s='('+input('arg=')+')'
 if abs(c)!=1:s+='^'+F(abs(c))
 if c>0:T.append(s)
 if c<0:B.append(s)
r='*'.join(T) or '1'
if B:r='('+r+')/('+'*'.join(B)+')'
print('=log_b('+r+')')
