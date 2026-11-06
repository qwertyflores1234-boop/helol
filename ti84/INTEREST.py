# Compound / continuous interest (E.2)
from math import *
E={'e':e,'pi':pi,'ln':log,'sqrt':sqrt,'exp':exp,'log':lambda v:log(v)/log(10)}
def N(m):
 while 1:
  try:return float(eval(input(m).lower().replace('^','**'),E))
  except:print('bad, retry')
def F(v):return '%.6g'%v
print('A=P(1+r/n)^(nt)')
print('n=0 means A=Pe^(rt)')
P=N('P=');r=N('rate %=')/100;n=N('n per yr=')
b=exp(r) if n==0 else (1+r/n)**n
print('APY='+F(100*b-100)+'%')
print('double in '+F(log(2)/log(b))+' yr')
while 1:
 c=input('1:A at t 2:t for A 0:quit ')
 if c=='1':t=N('t=');print('A='+F(P*b**t))
 if c=='2':A=N('A=');print('t='+F(log(A/P)/log(b)))
 if c=='0':break
