# EXPFN - E.1 & E.2 Exponential Functions
from math import *

def prep(s):
  s=s.replace(" ","").replace("^","**")
  o=""
  for i in range(len(s)):
    c=s[i]
    if i:
      p=s[i-1]
      if (p.isdigit() or p==")") and (c.isalpha() or c=="("):
        o+="*"
      elif p=="x" and c=="(" and (i<2 or not s[i-2].isalpha()):
        o+="*"
    o+=c
  return o

ENV={"e":e,"pi":pi,"sqrt":sqrt,"ln":log,"exp":exp}
ENV["log"]=lambda v:log(v)/log(10)

def num(m,blank=0):
  while 1:
    s=input(m).strip()
    if blank and s=="":
      return None
    try:
      return float(eval(prep(s),ENV))
    except:
      print("Bad input, retry")

def F(v):
  if abs(v)<1e-10:
    v=0.0
  return "%.6g"%v

def P():
  input("[enter]")

A=1.0
B=2.0

def y(x):
  return A*B**x

def info():
  k=log(B)
  print("y="+F(A)+"*"+F(B)+"^x")
  print("y="+F(A)+"*e^("+F(k)+"x)")
  print("a="+F(A)+" b="+F(B)+" k="+F(k))
  if B>1:
    print("GROWTH "+F((B-1)*100)+"% per x")
    print("Double time="+F(log(2)/k))
  elif B<1:
    print("DECAY "+F((1-B)*100)+"% per x")
    print("Half-life="+F(log(.5)/k))
  print("y-int (0,"+F(A)+") HA: y=0")
  print("Domain: all reals")
  print("Range: y>0" if A>0 else "Range: y<0")
  P()

def use():
  info()
  while 1:
    print("-- y="+F(A)+"*"+F(B)+"^x --")
    print("1:y at x   2:x for y")
    print("3:info     4:avg rate")
    print("5:x when y*factor")
    print("0:back")
    c=input("?").strip()
    if c=="1":
      x=num("x=")
      try:
        print("y="+F(y(x)))
      except:
        print("Undefined")
    elif c=="2":
      t=num("y=")
      if B<=0 or B==1 or t/A<=0:
        print("No solution")
      else:
        print("x=ln(y/a)/ln(b)")
        print("x="+F(log(t/A)/log(B)))
    elif c=="3":
      info()
      continue
    elif c=="4":
      p=num("x1=")
      q=num("x2=")
      if p==q:
        print("x1 must != x2")
      else:
        print("y1="+F(y(p))+" y2="+F(y(q)))
        print("avg rate="+F((y(q)-y(p))/(q-p)))
    elif c=="5":
      m=num("factor(2=double,.5=half)=")
      if m<=0 or B==1:
        print("No solution")
      else:
        print("time="+F(log(m)/log(B)))
    elif c=="0":
      return
    else:
      continue
    P()

def two_pts():
  global A,B
  x1=num("x1=")
  y1=num("y1=")
  x2=num("x2=")
  y2=num("y2=")
  if x1==x2 or y1==0 or y2/y1<=0:
    print("Can't fit those pts")
    P()
    return
  B=(y2/y1)**(1/(x2-x1))
  A=y1/B**x1
  print("b=(y2/y1)^(1/(x2-x1))")
  print(" =("+F(y2)+"/"+F(y1)+")^(1/"+F(x2-x1)+")")
  print(" ="+F(B))
  print("a=y1/b^x1="+F(A))
  P()
  use()

def start_pt():
  global A,B
  print("Initial value = a")
  A=num("a (at x=0)=")
  x=num("later x=")
  t=num("y at that x=")
  if A==0 or x==0 or t/A<=0:
    print("Can't fit that")
    P()
    return
  B=(t/A)**(1/x)
  print("b=(y/a)^(1/x)")
  print(" =("+F(t)+"/"+F(A)+")^(1/"+F(x)+")")
  print(" ="+F(B))
  P()
  use()

def start_rate():
  global A,B
  A=num("initial a=")
  r=num("rate %=")
  g=input("1:grows 2:decays?").strip()
  T=num("every how many x? (blank=1)",1)
  if T is None:
    T=1.0
  f=1+r/100 if g!="2" else 1-r/100
  B=f**(1/T)
  print("b=(1"+("+" if g!="2" else "-")+F(r/100)+")^(1/"+F(T)+")")
  print(" ="+F(B))
  P()
  use()

def start_fact():
  global A,B
  A=num("initial a=")
  m=num("factor(2=dbl,.5=half,3)=")
  T=num("every how many x=")
  if m<=0 or T==0:
    print("Bad values")
    P()
    return
  B=m**(1/T)
  print("b="+F(m)+"^(1/"+F(T)+")="+F(B))
  P()
  use()

def enter_ab():
  global A,B
  A=num("a=")
  B=num("b=")
  if B<=0:
    print("b must be > 0")
    P()
    return
  use()

def enter_ak():
  global A,B
  A=num("a=")
  k=num("k=")
  B=exp(k)
  print("b=e^k="+F(B))
  P()
  use()

def interest():
  global A,B
  print("A=P(1+r/n)^(nt)")
  print("cont: A=Pe^(rt)")
  p=num("P=")
  r=num("rate %=")/100
  n=num("n/yr(12=mo,0=cont)=")
  A=p
  B=exp(r) if n==0 else (1+r/n)**n
  print("per year b="+F(B))
  print("APY="+F((B-1)*100)+"%")
  print("x = years, y = $")
  P()
  use()

FACTS=[
"y=a*b^x  a=start(y-int)",
"b=growth factor, b>0",
"b>1 growth, 0<b<1 decay",
"grow r%: b=1+r  decay: b=1-r",
"(r as decimal: 5%=.05)",
"Domain all x, Range y>0",
"HA y=0, pts (0,a),(1,a*b)",
"2 pts: b=(y2/y1)^(1/(x2-x1))",
"       a=y1/b^x1",
"start a, pt(x,y): b=(y/a)^(1/x)",
"y=a*e^(kx): k=ln(b), b=e^k",
"double=ln2/ln b",
"half-life=ln(.5)/ln b",
"A=P(1+r/n)^(nt)  A=Pe^(rt)",
]

def facts():
  for i in range(len(FACTS)):
    print(FACTS[i])
    if i%9==8:
      P()
  P()

M=[two_pts,start_pt,start_rate,start_fact,enter_ab,enter_ak,interest,facts]
while 1:
  print("== EXPONENTIAL E.1/E.2 ==")
  print("1:2 points  2:start+pt")
  print("3:start+rate%")
  print("4:start+double/half")
  print("5:enter a,b  6:enter a,k")
  print("7:interest  8:facts")
  print("0:quit")
  c=input("?").strip()
  if c=="0":
    break
  if c in "12345678" and len(c)==1:
    M[int(c)-1]()
