# NLIN notes - enter=next b=back q=quit
T="""== F.1 LINEAR REG ==
y=mx+b
m=slope: y changes by m
 for each +1 in x
 ex 5.3 pts per hour
b=y-int: y when x=0
-- r (correlation) --
-1 <= r <= 1
r>0 positive (rises)
r<0 negative (falls)
|r|>=.8 strong
.5-.8 moderate, <.5 weak
r near 0: no LINEAR link
strongest = largest |r|
 -0.94 beats 0.72
-- R^2 --
R^2=r^2, from 0 to 1
r=-.8 -> R^2=.64
R^2=.81, neg slope: r=-.9
R^2 has NO sign/direction
close to 1 = good fit
-- CAUTION --
correlation != causation
U-shape: r~0 but strong
 NONlinear relationship
interpolation: x inside
 data range (reliable)
extrapolation: outside
 range (unreliable)
 ex score>100, price<0
-- PREDICT --
y: plug x into equation
x: x=(y-b)/m
-- EXCEL --
select data>Insert>
 Scatter. + button:
 Axis Titles, Chart Title
right-click point>Add
 Trendline>Linear>check
 Display Equation and
 Display R-squared
PROGRAM: RLIN (L1,L2)"""
L=T.split('\n');i=0
while i<len(L):
 for l in L[i:i+9]:print(l)
 c=input('enter=next b=back q=quit')
 if c=='q':break
 i=max(0,i-9) if c=='b' else i+9
