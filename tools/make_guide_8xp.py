import struct,sys
T={'A':0,'(':0x10,')':0x11,'"':0x2A,',':0x2B,' ':0x29,'.':0x3A,'+':0x70,'-':0x71,'*':0x82,'/':0x83,'^':0xF0,'=':0x6A,'<':0x6B,'>':0x6C,'?':0xAF,'!':0x2D}
def tstr(s):
  o=[]
  for c in s:
    if 'A'<=c<='Z' or '0'<=c<='9':o.append(ord(c))
    elif c in T and c!='A':o.append(T[c])
    else:raise Exception('bad char %r in %r'%(c,s))
  return o
NL=0x3F;DISP=0xDE;PAUSE=0xD8;CLR=0xE1;LBL=0xD6;GOTO=0xD7;MENU=0xE6;STOP=0xD9
code=[]
def line(*t):code.extend(t);code.append(NL)
def lbl(n):line(LBL,*tstr(n))
def goto(n):line(GOTO,*tstr(n))
def page(lines):
  assert len(lines)<=9,lines
  line(CLR)
  b=[DISP]
  for i,l in enumerate(lines):
    assert len(l)<=26,(len(l),l)
    if i:b.append(0x2B)
    b+= [0x2A]+tstr(l)+[0x2A]
  line(*b);line(PAUSE)
def menu(title,items):
  assert len(items)<=9
  b=[MENU,0x2A]+tstr(title)+[0x2A]
  for name,lab in items:b+=[0x2B,0x2A]+tstr(name)+[0x2A,0x2B]+tstr(lab)
  b.append(0x11);line(*b)

P=[
('EXP2PT','A',[[
"EXP2PT  (E.1, E.2)",
"FINDS Y=A*B^X THRU 2 PTS",
"USE FOR",
"-2 POINTS GIVEN",
"-START VALUE + A LATER",
" VALUE (X1=0, Y1=START)",
"-Y=B^X THRU 1 PT (X,Y)",
" TYPE 0,1 THEN X,Y",
"-PERCENT CHANGE FROM 2 PTS"],[
"EXP2PT OUTPUT",
"B AND A WITH FORMULAS",
"Y=A*B^X AND Y=A*E^(KX)",
"GROWTH OR DECAY PERCENT",
"DOUBLE TIME OR HALF-LIFE",
"THEN MENU",
" 1 = Y AT A GIVEN X",
" 2 = X (TIME) FOR A Y",
" 0 = QUIT"]]),
('EXPRATE','B',[[
"EXPRATE  (E.2)",
"MAKES Y=A*B^X FROM A START",
"VALUE PLUS A RATE",
"USE FOR",
"-GROWS R PERCENT PER YEAR",
"-DECAYS/DEPRECIATES R PCT",
"-DOUBLES/TRIPLES EVERY T",
"-HALF-LIFE T (FACTOR .5)",
"-CARBON DATING, MEDICINE"],[
"EXPRATE INPUTS",
"START A, THEN CHOOSE",
" 1 GROWS R PCT",
" 2 DECAYS R PCT",
" 3 FACTOR (2=DOUBLE,",
"   .5=HALF, 3=TRIPLE)",
"EVERY HOW MANY X (USU. 1)",
"SHOWS B, PCT, DOUBLE/HALF",
"1=Y AT X  2=X FOR Y"]]),
('INTEREST','C',[[
"INTEREST  (E.2)",
"A=P(1+R/N)^(NT)",
"N=0 MEANS CONTINUOUS",
"  A=P*E^(RT)",
"N= 1 YR, 4 QTR, 12 MONTH",
"   365 DAY",
"SHOWS APY, DOUBLE TIME",
"1=AMOUNT AFTER T YEARS",
"2=YEARS TO REACH AMOUNT"]]),
('CONVBK','D',[[
"CONVBK  (E.2, F.2)",
"CONVERTS EXPONENTIAL FORMS",
"1  A*B^X  TO  A*E^(KX)",
"   K=LN(B)",
"2  A*E^(KX)  TO  A*B^X",
"   B=E^K",
"USE FOR EXCEL EXPONENTIAL",
"TRENDLINES AND FINDING THE",
"GROWTH/DECAY PERCENT"]]),
('LOGB','E',[[
"LOGB  (E.3)",
"LOG B(X)=Y  MEANS  B^Y=X",
"TYPE B, X, Y AND LEAVE",
"THE UNKNOWN BLANK",
"USE FOR",
"-EVALUATE LOGS (Y BLANK)",
"-LOG TO EXP FORM + BACK",
"-CHANGE OF BASE VALUES",
"-B=E FOR LN. 1/9 OK"]]),
('EXPSOLVE','F',[[
"EXPSOLVE  (E.4)",
"SOLVES A*B^(CX+D)+F=K",
"WITH STEPS",
"USE FOR ONE EXPONENTIAL",
"EX 7(1.4)^X=30",
" A=7 B=1.4 C=1 D=0 F=0",
" K=30",
"EX 4E^(.3X)+2=18",
" A=4 B=E C=.3 D=0 F=2"]]),
('LOGSOLVE','G',[[
"LOGSOLVE  (E.4)",
"SOLVES A*LOG B(CX+D)+F=K",
"WITH STEPS",
"USE FOR ONE LOG OR LN",
"EX LOG3(X-2)=4",
" A=1 B=3 C=1 D=-2 F=0 K=4",
"EX 2LN(X)-3=7",
" A=2 B=E C=1 D=0 F=-3",
" K=7"]]),
('EQSOLVE','H',[[
"EQSOLVE  (E.4)",
"SOLVES ANY EQUATION",
"TYPE LEFT SIDE, RIGHT SIDE",
"AND A SEARCH RANGE",
"USE FOR",
"-MANY LOGS (REJECTS",
" EXTRANEOUS ANSWERS)",
"-DIFFERENT BASES 4^X=9^X",
"-WHEN BALL HITS GROUND"],[
"EQSOLVE TYPING",
"LN(X)  LOG(X)=BASE 10",
"LOGB(2,X) = LOG BASE 2",
"E^X   2X OK   ^ FOR POWER",
"LOGS  RANGE 0 TO 50",
"OTHERS  -20 TO 20",
"CAPS OR LOWERCASE BOTH OK",
"2ND ALPHA = LETTER LOCK",
"NONE FOUND=WIDEN RANGE"]]),
('LOGINFO','I',[[
"LOGINFO  (E.3)",
"FOR Y=A*LOG B(X-H)+K",
"SHOWS DOMAIN, RANGE, VA,",
"X-INT, Y-INT, INC/DEC,",
"AND THE INVERSE",
"X+4 MEANS H=-4",
"PLAIN LOG2(X)",
" A=1 B=2 H=0 K=0",
"INVERSE OF LOG = EXP"]]),
('EXPINFO','J',[[
"EXPINFO  (E.1, E.3)",
"FOR Y=A*B^(X-H)+K",
"SHOWS DOMAIN, RANGE, HA,",
"Y-INT, X-INT, INVERSE",
"USE FOR GRAPH QUESTIONS",
"AND INVERSE OF EXP FNS",
"EX 2(3)^X",
" A=2 B=3 H=0 K=0",
"INC IF B>1, DEC IF B<1"]]),
('CONDENSE','K',[[
"CONDENSE  (E.3, E.4)",
"COMBINES LOGS INTO ONE",
"TYPE NUMBER OF TERMS, THEN",
"EACH COEF AND INSIDE",
"EX 2LOGX+LOGY-3LOGZ",
" 3 TERMS",
" 2,X  1,Y  -3,Z",
"GIVES LOG(X^2*Y/Z^3)",
"LOG B MEANS SAME BASE"]]),
('RLIN','L',[[
"RLIN  (F.1)",
"LINEAR REGRESSION Y=MX+B",
"SHOWS SLOPE, INTERCEPT,",
"R, R^2, STRONG/WEAK AND",
"POSITIVE/NEGATIVE",
"DATA X IN L1, Y IN L2",
"(STAT, EDIT) THEN ENTER",
"1=PREDICT Y AT X",
"2=X NEEDED FOR A Y"]]),
('RPOLY','M',[[
"RPOLY  (F.2)",
"QUADRATIC / POLYNOMIAL",
"REGRESSION LIKE EXCEL",
"DEGREE 2=QUADRATIC",
"DEGREE 3=CUBIC (UP TO 6)",
"SHOWS EACH COEFFICIENT",
"AND R^2",
"1=PREDICT Y AT X",
"X FOR Y USE EQSOLVE"]]),
('REXP','N',[[
"REXP  (F.2)",
"EXPONENTIAL REGRESSION",
"LIKE EXCEL",
"SHOWS Y=A*E^(KX) AND",
"Y=A*B^X, B=E^K, R^2",
"GROWTH PCT = B-1",
"NEEDS ALL Y>0",
"1=PREDICT Y AT X",
"2=X NEEDED FOR A Y"]]),
('RLOG','O',[[
"RLOG  (F.2)",
"LOG REGRESSION LIKE EXCEL",
"Y=C*LN(X)+B AND R^2",
"NEEDS ALL X>0",
"X LIKE E^2 OK IN LIST",
"1=PREDICT Y AT X",
"2=X NEEDED FOR A Y",
"",
"RPOW = POWER Y=A*X^P"]]),
('RPOW','P',[[
"RPOW  (F.2 BONUS)",
"POWER REGRESSION",
"LIKE EXCEL Y=A*X^P",
"SHOWS A, P, R^2",
"NEEDS ALL X>0 AND Y>0",
"1=PREDICT Y AT X",
"2=X NEEDED FOR A Y",
"",
"COMPARE R^2 TO PICK BEST"]]),
]
assert len(P)==16-1+1 or True
# main
assert len(P)==16 and len(set(l for _,l,_ in P))==16
page(["HOW TO RUN A PROGRAM",
"APPS, PYTHON, PICK FILE,",
"PRESS Y= (RUN)",
"PRESS ENTER AFTER INPUTS",
"0 = QUIT/BACK",
"ON KEY STOPS A FROZEN ONE",
"NOTES  NINDEX NEXP1 NEXP2",
" NLOG1 NLOG2 NEQ NLIN",
" NNONLIN"])
lbl('MA')
menu('PYTHON GUIDE 1',[(n,l) for n,l,_ in P[:8]]+[('MORE','MB')])
lbl('MB')
menu('PYTHON GUIDE 2',[(n,l) for n,l,_ in P[8:]]+[('QUIT','QQ')])
for i,(n,l,pages) in enumerate(P):
  lbl(l)
  for pg in pages:page(pg)
  goto('MA' if i<8 else 'MB')
lbl('QQ')
line(CLR)
code.append(STOP)
data=bytes(code)
name=b'GUIDE'
vd=struct.pack('<H',len(data))+data
entry=struct.pack('<HH',13,len(vd))+bytes([5])+name.ljust(8,b'\0')+bytes([0,0])+struct.pack('<H',len(vd))+vd
hdr=b'**TI83F*\x1a\x0a\x00'+b'Python program guide'.ljust(42,b'\0')+struct.pack('<H',len(entry))
out=hdr+entry+struct.pack('<H',sum(entry)&0xFFFF)
open(sys.argv[1],'wb').write(out)
print('ok',len(out),'bytes, tokens',len(data))
