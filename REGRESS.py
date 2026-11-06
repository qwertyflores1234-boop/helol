# REGRESS - F.1 & F.2 Linear and Nonlinear Regression
# Matches Excel trendlines (exp/log/power R^2 like Excel)
from math import *

def num(m,blank=0):
  while 1:
    s=input(m).strip()
    if blank and s=="":
      return None
    try:
      return float(eval(s.replace("^","**"),{"e":e,"pi":pi}))
    except:
      print("Bad input, retry")

def F(v):
  if abs(v)<1e-10:
    v=0.0
  return "%.6g"%v

def pm(v):
  return "+"+F(v) if v>=0 else "-"+F(-v)

def P():
  input("[enter]")

X=[]
Y=[]
MF=None
MS=["(no model yet)"]

def nums(m):
  while 1:
    s=input(m).strip().replace(" ","")
    try:
      return [float(eval(t.replace("^","**"),{"e":e})) for t in s.split(",") if t!=""]
    except:
      print("Bad list, retry")

def enter():
  global X,Y
  print("Type values with commas")
  print("ex: 1,2,3,4")
  while 1:
    X=nums("x's: ")
    Y=nums("y's: ")
    if len(X)==len(Y) and len(X)>1:
      break
    print("Need same count, >=2")
  print(str(len(X))+" points saved")
  P()

def load():
  global X,Y
  try:
    from ti_system import recall_list
    X=[float(v) for v in recall_list("1")]
    Y=[float(v) for v in recall_list("2")]
    print("Loaded "+str(len(X))+" pts L1,L2")
    if len(X)!=len(Y):
      print("L1,L2 sizes differ!")
  except:
    print("Can't read L1/L2 here")
  P()

def show():
  for i in range(len(X)):
    print(F(X[i])+" , "+F(Y[i]))
    if i%9==8:
      P()
  P()

def lin(u,v):
  n=len(u)
  mu=sum(u)/n
  mv=sum(v)/n
  sxx=sum((a-mu)**2 for a in u)
  syy=sum((b-mv)**2 for b in v)
  sxy=sum((u[i]-mu)*(v[i]-mv) for i in range(n))
  m=sxy/sxx
  r=sxy/sqrt(sxx*syy) if syy>0 else 1.0
  return m,mv-m*mu,r

def r2(f):
  n=len(Y)
  my=sum(Y)/n
  st=sum((b-my)**2 for b in Y)
  se=sum((Y[i]-f(X[i]))**2 for i in range(n))
  return 1-se/st if st>0 else 1.0

def ok(n=2):
  if len(X)<n:
    print("Need >= "+str(n)+" points")
    P()
    return 0
  return 1

def setm(f,s):
  global MF,MS
  MF=f
  MS=s
  for t in s:
    print(t)
  P()

def corr(r):
  a=abs(r)
  if a<0.1:
    return "no correlation"
  w="strong" if a>=0.8 else ("moderate" if a>=0.5 else "weak")
  return w+(" positive" if r>0 else " negative")

def f_lin():
  if not ok():
    return
  m,b,r=lin(X,Y)
  setm(lambda x:m*x+b,["LINEAR y=mx+b",
   "y="+F(m)+"x"+pm(b),"m(slope)="+F(m),"b(y-int)="+F(b),
   "r="+F(r),"R^2="+F(r*r),corr(r)])

def gauss(M,v):
  n=len(v)
  for i in range(n):
    p=max(range(i,n),key=lambda j:abs(M[j][i]))
    M[i],M[p]=M[p],M[i]
    v[i],v[p]=v[p],v[i]
    for j in range(i+1,n):
      t=M[j][i]/M[i][i]
      for k in range(i,n):
        M[j][k]-=t*M[i][k]
      v[j]-=t*v[i]
  c=[0.0]*n
  for i in range(n-1,-1,-1):
    c[i]=(v[i]-sum(M[i][k]*c[k] for k in range(i+1,n)))/M[i][i]
  return c

def pfit(d):
  n=len(X)
  mx=sum(X)/n
  s=max(abs(a-mx) for a in X) or 1.0
  T=[(a-mx)/s for a in X]
  M=[[sum(t**(i+j) for t in T) for j in range(d+1)] for i in range(d+1)]
  v=[sum(Y[k]*T[k]**i for k in range(n)) for i in range(d+1)]
  c=gauss(M,v)
  p=[c[d]]
  for i in range(d-1,-1,-1):
    q=[0.0]*(len(p)+1)
    for j in range(len(p)):
      q[j+1]+=p[j]/s
      q[j]-=p[j]*mx/s
    q[0]+=c[i]
    p=q
  return p

def pstr(p):
  s=""
  for i in range(len(p)-1,-1,-1):
    c=p[i]
    t=F(abs(c))
    if i>1:
      t+="x^"+str(i)
    elif i==1:
      t+="x"
    if s=="":
      s="-"+t if c<0 else t
    else:
      s+=("-" if c<0 else "+")+t
  return "y="+s

def peval(p,x):
  r=0.0
  for c in reversed(p):
    r=r*x+c
  return r

def f_poly(d=0):
  if d==0:
    d=int(num("degree (2-6)="))
  if d<1 or d>6 or not ok(d+1):
    if d<1 or d>6:
      print("degree 1 to 6")
      P()
    return
  try:
    p=pfit(d)
  except:
    print("Can't fit (repeat x?)")
    P()
    return
  f=lambda x:peval(p,x)
  nm="QUADRATIC" if d==2 else "POLY deg "+str(d)
  s=[nm,pstr(p)]
  for i in range(d,-1,-1):
    s.append("x^"+str(i)+" coef: "+F(p[i]))
  s.append("R^2="+F(r2(f)))
  setm(f,s)

def f_exp():
  if not ok():
    return
  if min(Y)<=0:
    print("Exp needs all y>0")
    P()
    return
  k,c,r=lin(X,[log(v) for v in Y])
  a=exp(c)
  b=exp(k)
  setm(lambda x:a*exp(k*x),["EXPONENTIAL (Excel)",
   "y="+F(a)+"e^("+F(k)+"x)","a="+F(a)+" k="+F(k),
   "b-form: y="+F(a)+"*"+F(b)+"^x","b=e^k="+F(b),
   "R^2="+F(r*r)])

def f_log():
  if not ok():
    return
  if min(X)<=0:
    print("Log needs all x>0")
    P()
    return
  c,b,r=lin([log(v) for v in X],Y)
  setm(lambda x:c*log(x)+b,["LOGARITHMIC (Excel)",
   "y="+F(c)+"ln(x)"+pm(b),"R^2="+F(r*r)])

def f_pow():
  if not ok():
    return
  if min(X)<=0 or min(Y)<=0:
    print("Power needs x>0,y>0")
    P()
    return
  p,c,r=lin([log(v) for v in X],[log(v) for v in Y])
  a=exp(c)
  setm(lambda x:a*x**p,["POWER (Excel)",
   "y="+F(a)+"x^"+F(p),"R^2="+F(r*r)])

def best():
  if not ok(3):
    return
  R=[]
  m,b,r=lin(X,Y)
  R.append(("linear",r*r))
  for d in (2,3):
    if len(X)>d:
      p=pfit(d)
      R.append(("poly"+str(d),r2(lambda x:peval(p,x))))
  if min(Y)>0:
    R.append(("exp",lin(X,[log(v) for v in Y])[2]**2))
  if min(X)>0:
    R.append(("log",lin([log(v) for v in X],Y)[2]**2))
  if min(X)>0 and min(Y)>0:
    R.append(("power",lin([log(v) for v in X],[log(v) for v in Y])[2]**2))
  for t in R:
    print(t[0]+": R^2="+F(t[1]))
  print("Highest R^2 fits best")
  P()

def sf(x):
  try:
    return float(MF(x))
  except:
    return None

def predict():
  if MF is None:
    print("Fit a model first")
    P()
    return
  while 1:
    print(MS[1])
    print("1:y at x  2:x for y")
    print("0:back")
    c=input("?").strip()
    if c=="0":
      return
    if c=="1":
      x=num("x=")
      v=sf(x)
      print("undefined" if v is None else "y="+F(v))
      P()
    elif c=="2":
      t=num("y=")
      lo=min(X)
      hi=max(X)
      w=(hi-lo) or 1.0
      a=num("from x (blank auto)=",1)
      b=num("to x (blank auto)=",1)
      if a is None:
        a=lo-5*w
      if b is None:
        b=hi+5*w
      print("Working...")
      N=400
      h=(b-a)/N
      out=[]
      x0=a
      y0=sf(a)
      for i in range(1,N+1):
        x1=a+i*h
        y1=sf(x1)
        if y0 is not None and y1 is not None and (y0-t<0)!=(y1-t<0):
          p,q=x0,x1
          for _ in range(60):
            m=(p+q)/2
            v=sf(m)
            if v is None:
              break
            if (v-t<0)==(y0-t<0):
              p=m
            else:
              q=m
          out.append((p+q)/2)
        elif y0 is not None and y0==t:
          out.append(x0)
        x0,y0=x1,y1
      if not out:
        print("None in "+F(a)+".."+F(b))
      for r in out:
        print("x="+F(r))
      P()

def conv():
  print("1:a*b^x -> a*e^(kx)")
  print("2:a*e^(kx) -> a*b^x")
  c=input("?").strip()
  a=num("a=")
  if c=="2":
    k=num("k=")
    print("b=e^k="+F(exp(k)))
    print("y="+F(a)+"*"+F(exp(k))+"^x")
  else:
    b=num("b=")
    if b<=0:
      print("b must be > 0")
    else:
      print("k=ln(b)="+F(log(b)))
      print("y="+F(a)+"e^("+F(log(b))+"x)")
  P()

def plot():
  if MF is None or not ok():
    return
  try:
    import ti_plotlib as plt
    x0=min(X)
    x1=max(X)
    w=(x1-x0) or 1
    x0-=w*.1
    x1+=w*.1
    xs=[x0+i*(x1-x0)/40 for i in range(41)]
    ys=[sf(v) for v in xs]
    g=[v for v in ys+Y if v is not None]
    y0=min(g)
    y1=max(g)
    hy=(y1-y0) or 1
    plt.cls()
    plt.window(x0,x1,y0-hy*.1,y1+hy*.1)
    plt.axes("on")
    plt.color(0,0,255)
    plt.scatter(X,Y,"o")
    plt.color(255,0,0)
    for i in range(40):
      if ys[i] is not None and ys[i+1] is not None:
        plt.line(xs[i],ys[i],xs[i+1],ys[i+1],"")
    plt.show_plot()
  except:
    print("Plot not available")
    P()

FACTS=[
"r: -1 to 1 (correlation)",
"r>0 positive: y up as x up",
"r<0 negative: y down as x up",
"r near 0: no correlation",
"|r|>=.8 strong, .5-.8 mod",
"R^2=r^2, closer to 1=better",
"R^2 near 1: strong correlat.",
"Correlation != causation",
"Predict: plug x in trendline",
"EXCEL: select data> Insert>",
" Scatter. Click pt> Add",
" Trendline> pick type> check",
" Display Equation & R^2.",
" Add Chart Title + Axis Titles",
"Excel exp: y=ae^(kx)",
" to b-form: b=e^k",
" from b-form: k=ln(b)",
"Excel log: y=c*ln(x)+b",
"Poly: order 2=quad, 3=cubic",
]

def facts():
  for i in range(len(FACTS)):
    print(FACTS[i])
    if i%9==8:
      P()
  P()

M=[enter,load,show,f_lin,lambda:f_poly(2),f_poly,f_exp,f_log,f_pow,best,predict,conv,plot,facts]
while 1:
  print("== REGRESSION F.1/F.2 ==")
  print("1:enter 2:load L1L2 3:show")
  print("4:LINEAR  5:QUADRATIC")
  print("6:POLY  7:EXPON  8:LOG")
  print("9:POWER  10:compare R^2")
  print("11:predict 12:convert b/k")
  print("13:plot 14:facts 0:quit")
  c=input("?").strip()
  if c=="0":
    break
  try:
    i=int(c)-1
  except:
    continue
  if 0<=i<len(M):
    M[i]()
