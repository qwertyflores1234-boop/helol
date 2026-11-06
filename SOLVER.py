# SOLVER - function solver for TI-84 Plus CE Python
# Type a function of x, then pick what to do with it.
# Examples:  x^2-4   2x^3-x+1   sin(x)-x/2   e^x-3
from math import *

W = 200  # samples used when scanning for roots


def prep(s):
  # make calculator-style input valid Python
  s = s.replace(" ", "").replace("^", "**")
  out = ""
  for i in range(len(s)):
    c = s[i]
    if i > 0:
      p = s[i - 1]
      # implicit multiply: 2x  2(x+1)  )(  )x
      if (p.isdigit() or p == ")") and (c.isalpha() or c == "("):
        out += "*"
      # x(...)  -> x*(...)
      elif p == "x" and c == "(" and (i < 2 or not s[i - 2].isalpha()):
        out += "*"
    out += c
  return out


ENV = {}
for k in ("sin", "cos", "tan", "asin", "acos", "atan", "sqrt",
          "log", "exp", "pi", "e", "fabs", "floor", "ceil"):
  ENV[k] = eval(k)
ENV["abs"] = fabs
ENV["ln"] = log  # natural log


def log10_(v):
  return log(v) / log(10)


ENV["log"] = log10_  # log = base 10, like the TI keys

expr = ""


def f(x):
  ENV["x"] = x
  return eval(expr, ENV)


def num(msg):
  while True:
    s = input(msg)
    try:
      return float(eval(prep(s), ENV))
    except Exception:
      print("Bad number, retry")


def fmt(v):
  if abs(v) < 1e-10:
    v = 0.0
  return str(round(v, 6))


def pause():
  input("[enter]")


def safe(x):
  try:
    return f(x)
  except Exception:
    return None


def roots_of(g, a, b):
  # scan [a,b] for sign changes of g, refine with bisection
  res = []
  h = (b - a) / W
  x0 = a
  y0 = g(x0)
  for i in range(1, W + 1):
    x1 = a + i * h
    y1 = g(x1)
    if y0 is not None and y1 is not None:
      if y0 == 0:
        res.append(x0)
      elif (y0 < 0) != (y1 < 0):
        r = bisect_g(g, x0, x1, y0)
        if r is not None:
          res.append(r)
    x0, y0 = x1, y1
  if y0 == 0:
    res.append(x0)
  # remove duplicates
  out = []
  for r in res:
    if not out or abs(r - out[-1]) > 1e-7:
      out.append(r)
  return out


def bisect_g(g, a, b, ga):
  for _ in range(60):
    m = (a + b) / 2
    gm = g(m)
    if gm is None:
      return None
    if gm == 0:
      return m
    if (ga < 0) == (gm < 0):
      a, ga = m, gm
    else:
      b = m
  m = (a + b) / 2
  gm = g(m)
  # reject jumps like tan(x) asymptotes
  if gm is None or abs(gm) > 1e-4:
    return None
  return m


def deriv(x):
  h = 1e-5 * max(1, abs(x))
  return (f(x + h) - f(x - h)) / (2 * h)


def sderiv(x):
  try:
    return deriv(x)
  except Exception:
    return None


def integ(a, b, n=200):
  h = (b - a) / n
  s = f(a) + f(b)
  for i in range(1, n):
    s += (4 if i % 2 else 2) * f(a + i * h)
  return s * h / 3


def new_func():
  global expr
  while True:
    s = input("f(x)=")
    try:
      expr = prep(s)
      ENV["x"] = 1.2345
      eval(expr, ENV)
      return
    except ZeroDivisionError:
      return
    except ValueError:
      return
    except Exception:
      print("Can't read that.")
      print("Use * ^ ( ) x sin ln")


def do_eval():
  x = num("x=")
  try:
    print("f(x)=" + fmt(f(x)))
  except Exception:
    print("Undefined there")
  pause()


def do_roots():
  print("Search interval:")
  a = num("from a=")
  b = num("to b=")
  if a > b:
    a, b = b, a
  r = roots_of(safe, a, b)
  if not r:
    print("No roots found")
  for v in r:
    print("x=" + fmt(v))
  pause()


def do_deriv():
  x = num("at x=")
  try:
    print("f'(x)=" + fmt(deriv(x)))
  except Exception:
    print("Undefined there")
  pause()


def do_integ():
  a = num("lower a=")
  b = num("upper b=")
  try:
    print("Integral=" + fmt(integ(a, b)))
  except Exception:
    print("Undefined in range")
  pause()


def do_table():
  a = num("start x=")
  d = num("step=")
  for i in range(8):
    x = a + i * d
    y = safe(x)
    print(fmt(x) + " | " + ("undef" if y is None else fmt(y)))
  pause()


def do_extrema():
  print("Search interval:")
  a = num("from a=")
  b = num("to b=")
  if a > b:
    a, b = b, a
  r = roots_of(sderiv, a, b)
  if not r:
    print("None found")
  for v in r:
    d2 = (sderiv(v + 1e-4) or 0) - (sderiv(v - 1e-4) or 0)
    kind = "min" if d2 > 0 else ("max" if d2 < 0 else "flat")
    y = safe(v)
    print(kind + " (" + fmt(v) + "," + ("?" if y is None else fmt(y)) + ")")
  pause()


def do_quad():
  print("ax^2+bx+c=0")
  a = num("a=")
  b = num("b=")
  c = num("c=")
  if a == 0:
    if b == 0:
      print("No x to solve")
    else:
      print("x=" + fmt(-c / b))
    pause()
    return
  d = b * b - 4 * a * c
  print("Discrim=" + fmt(d))
  if d >= 0:
    print("x1=" + fmt((-b + sqrt(d)) / (2 * a)))
    print("x2=" + fmt((-b - sqrt(d)) / (2 * a)))
  else:
    re = -b / (2 * a)
    im = sqrt(-d) / (2 * abs(a))
    print("x=" + fmt(re) + " +/- " + fmt(im) + "i")
  pause()


def do_system():
  print("ax+by=c")
  print("dx+ey=f")
  a = num("a=")
  b = num("b=")
  c = num("c=")
  d = num("d=")
  e_ = num("e=")
  f_ = num("f=")
  det = a * e_ - b * d
  if det == 0:
    print("No unique solution")
  else:
    print("x=" + fmt((c * e_ - b * f_) / det))
    print("y=" + fmt((a * f_ - c * d) / det))
  pause()


def menu():
  print("f(x)=" + expr[:26])
  print("1:Eval   2:Roots")
  print("3:Deriv  4:Integral")
  print("5:Table  6:Min/Max")
  print("7:Quadratic 8:2x2 Sys")
  print("9:New f(x) 0:Quit")
  return input("Choice:")


print("== FUNCTION SOLVER ==")
new_func()
acts = {"1": do_eval, "2": do_roots, "3": do_deriv, "4": do_integ,
        "5": do_table, "6": do_extrema, "7": do_quad, "8": do_system,
        "9": new_func}
while True:
  ch = menu().strip()
  if ch == "0":
    break
  if ch in acts:
    acts[ch]()
print("Bye!")
