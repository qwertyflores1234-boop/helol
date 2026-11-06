# Solve ANY equation L(x)=R(x) numerically (E.4)
# ln() log() logb(b,x) e^x  2x ok
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
E['logb']=lambda b,v:log(v)/log(b)
def P(s):
 s=s.replace(' ','').replace('^','**');o=''
 for i in range(len(s)):
  c=s[i]
  if i and (s[i-1].isdigit() or s[i-1]==')') and (c.isalpha() or c=='('):o+='*'
  o+=c
 return o
g=eval('lambda x:('+P(input('Left: '))+')-('+P(input('Right: '))+')',E)
def G(x):
 try:return float(g(x))
 except:return None
a=N('from x= ');b=N('to x= ')
print('working...')
h=(b-a)/300;R=[];y=G(a)
for i in range(1,301):
 p=a+(i-1)*h;q=p+h;z=G(q)
 if y==0:R.append(p)
 elif y!=None and z!=None and z!=0 and (y<0)!=(z<0):
  u=y
  for j in range(50):
   m=(p+q)/2;w=G(m)
   if w==None:break
   if (w<0)==(u<0):p=m
   else:q=m
  if w!=None and abs(w)<1e-4:R.append(m)
 y=z
if y==0:R.append(b)
for r in R:print('x='+F(r))
if not R:print('none in range')
