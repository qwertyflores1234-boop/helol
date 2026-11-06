# LOGEQ - E.3 & E.4 Logs and Log/Exp Equations
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

def lg(v):
  return log(v)/log(10)

def logb(b,v):
  return log(v)/log(b)

ENV={"e":e,"pi":pi,"sqrt":sqrt,"ln":log,"exp":exp,"log":lg,"logb":logb}

def num(m,blank=0):
  while 1:
    s=input(m).strip()
    if blank and s=="":
      return None
    try:
      return float(eval(prep(s),ENV))
    except:
      print("Bad input, retry")

def base():
  while 1:
    b=num("base b (e ok)=")
    if b>0 and b!=1:
      return b
    print("b>0 and b!=1")

def F(v):
  if abs(v)<1e-10:
    v=0.0
  return "%.6g"%v

def bn(b):
  if abs(b-e)<1e-9:
    return "e"
  return F(b)

def mn(v):
  return "-"+F(v) if v>=0 else "+"+F(-v)

def P():
  input("[enter]")

def evlog():
  b=base()
  x=num("x=")
  if x<=0:
    print("x must be > 0")
  else:
    print("log_"+bn(b)+"("+F(x)+")")
    print("=ln("+F(x)+")/ln("+bn(b)+")")
    print("="+F(logb(b,x)))
  P()

def convert():
  print("log_b(x)=y <=> b^y=x")
  print("leave unknown blank")
  b=num("b=",1)
  x=num("x=",1)
  t=num("y=",1)
  try:
    if b is None:
      b=x**(1/t)
    elif x is None:
      x=b**t
    elif t is None:
      t=logb(b,x)
    print("log_"+bn(b)+"("+F(x)+")="+F(t))
    print(bn(b)+"^"+F(t)+"="+F(x))
  except:
    print("No solution")
  P()

def exp_eq():
  print("a*b^(cx+d)+f=k")
  a=num("a=")
  b=base()
  c=num("c=")
  d=num("d=")
  f=num("f=")
  k=num("k=")
  v=(k-f)/a
  print(bn(b)+"^(cx+d)=(k-f)/a="+F(v))
  if v<=0:
    print("No solution (b^ >0)")
  else:
    u=logb(b,v)
    print("cx+d=log_"+bn(b)+"("+F(v)+")")
    print("    ="+F(u))
    if c==0:
      print("c=0: no x")
    else:
      print("x=("+F(u)+mn(d)+")/"+F(c))
      print("x="+F((u-d)/c))
  P()

def log_eq():
  print("a*log_b(cx+d)+f=k")
  a=num("a=")
  b=base()
  c=num("c=")
  d=num("d=")
  f=num("f=")
  k=num("k=")
  v=(k-f)/a
  print("log_"+bn(b)+"(cx+d)="+F(v))
  u=b**v
  print("cx+d="+bn(b)+"^"+F(v)+"="+F(u))
  if c==0:
    print("c=0: no x")
  else:
    print("x="+F((u-d)/c))
  P()

def safe(g,x):
  try:
    return float(g(x))
  except:
    return None

def solve():
  print("Solve L(x)=R(x)")
  print("ln() log() logb(b,x) e^x")
  L=prep(input("Left: "))
  R=prep(input("Right: "))
  def g(x):
    ENV["x"]=x
    return eval(L,ENV)-eval(R,ENV)
  a=num("from x (blank -20)=",1)
  b=num("to x (blank 20)=",1)
  if a is None:
    a=-20.0
  if b is None:
    b=20.0
  if a>b:
    a,b=b,a
  print("Working...")
  N=400
  h=(b-a)/N
  res=[]
  x0=a
  y0=safe(g,x0)
  for i in range(1,N+1):
    x1=a+i*h
    y1=safe(g,x1)
    if y0 is not None and y0==0:
      res.append(x0)
    elif y0 is not None and y1 is not None and (y0<0)!=(y1<0):
      p,q,gp=x0,x1,y0
      for _ in range(60):
        m=(p+q)/2
        gm=safe(g,m)
        if gm is None:
          break
        if (gp<0)==(gm<0):
          p,gp=m,gm
        else:
          q=m
      m=(p+q)/2
      gm=safe(g,m)
      if gm is not None and abs(gm)<1e-4:
        res.append(m)
    x0,y0=x1,y1
  if y0==0:
    res.append(x0)
  out=[]
  for r in res:
    if not out or abs(r-out[-1])>1e-6:
      out.append(r)
  if not out:
    print("No solution in range")
  for r in out:
    print("x="+F(r))
  P()

def loginfo():
  print("y=a*log_b(x-h)+k")
  a=num("a=")
  b=base()
  h=num("h=")
  k=num("k=")
  print("Domain: x>"+F(h))
  print("Range: all reals")
  print("VA: x="+F(h))
  print("x-int: x="+F(h+b**(-k/a)))
  if h<0:
    print("y-int: y="+F(a*logb(b,-h)+k))
  up=(b>1)==(a>0)
  print("increasing" if up else "decreasing")
  print("inverse: y="+bn(b)+"^((x"+mn(k)+")/"+F(a)+")"+mn(-h))
  P()

def expinfo():
  print("y=a*b^(x-h)+k")
  a=num("a=")
  b=base()
  h=num("h=")
  k=num("k=")
  print("Domain: all reals")
  print("Range: y"+(">" if a>0 else "<")+F(k))
  print("HA: y="+F(k))
  print("y-int: y="+F(a*b**(-h)+k))
  v=-k/a
  if v>0:
    print("x-int: x="+F(h+logb(b,v)))
  else:
    print("no x-int")
  print("inverse:")
  print("y=log_"+bn(b)+"((x"+mn(k)+")/"+F(a)+")"+mn(-h))
  P()

def condense():
  print("c1*log(A)+c2*log(B)...")
  print("same base, coef,arg")
  n=int(num("# of terms="))
  top=[]
  bot=[]
  for i in range(n):
    c=num("coef "+str(i+1)+"=")
    s=input("arg "+str(i+1)+"=").strip()
    t="("+s+")"
    if abs(c)!=1:
      t+="^"+F(abs(c))
    if c>0:
      top.append(t)
    elif c<0:
      bot.append(t)
  r="*".join(top) if top else "1"
  if bot:
    r="("+r+")/("+"*".join(bot)+")"
  print("= log_b( "+r+" )")
  P()

FACTS=[
"log_b(x)=y means b^y=x",
"ln=log base e, log=base 10",
"log_b(1)=0  log_b(b)=1",
"log_b(b^x)=x  b^(log_b x)=x",
"y=log_b(x) inverse of b^x",
"Dom x>0, Range all, VA x=0",
"pts (1,0),(b,1),(1/b,-1)",
"b>1 incr, 0<b<1 decr",
"POWER: log(x^p)=p*log(x)",
"PRODUCT: log(xy)=logx+logy",
"QUOTIENT: log(x/y)=logx-logy",
"CHANGE BASE: log_b x=lnx/lnb",
"Exp eq: isolate b^(),",
"  then take log of both sides",
"Log eq: isolate log, rewrite",
"  as b^y=x, CHECK x in domain",
"Many logs: condense to one",
]

def facts():
  for i in range(len(FACTS)):
    print(FACTS[i])
    if i%9==8:
      P()
  P()

M=[evlog,convert,exp_eq,log_eq,solve,loginfo,expinfo,condense,facts]
while 1:
  print("== LOGS E.3/E.4 ==")
  print("1:log_b(x)  2:log<->exp")
  print("3:solve a*b^(cx+d)+f=k")
  print("4:solve a*log(cx+d)+f=k")
  print("5:solve ANY equation")
  print("6:log fn info/inverse")
  print("7:exp fn info/inverse")
  print("8:condense logs 9:facts")
  print("0:quit")
  c=input("?").strip()
  if c=="0":
    break
  if len(c)==1 and c in "123456789":
    M[int(c)-1]()
