import math

ax=int(input("Point A X: "))
ay=int(input("Point A Y: "))
bx=int(input("Point B X: "))
by=int(input("Point B Y: "))
cx=int(input("Point C X: "))
cy=int(input("Point C Y: "))

if bx != ax:
  absl = ((by - ay) / (bx - ax))
  abfor = "AB Formula: y = " + str(absl) + "x + " + str(ay - absl * ax)
else:
  abfor = "AB Formula: x = " + str(ax)

if bx != cx:
  bcsl = ((by - cy) / (bx - cx))
  bcfor = "BC Formula: y = " + str(bcsl) + "x + " + str(by - bcsl * bx)
else:
  bcfor = "BC Formula: x = " + str(bx)

if cx != ax:
  acsl = ((cy - ay) / (cx - ax))
  acfor = "AC Formula: y = " + str(acsl) + "x + " + str(cy - acsl * cx)
else:
  acfor = "AC Formula: x = " + str(cx)

ab=math.sqrt((ax-bx)**2+(ay-by)**2)
bc=math.sqrt((bx-cx)**2+(by-cy)**2)
ac=math.sqrt((ax-cx)**2+(ay-cy)**2)
perimeter=ab+bc+ac
s=perimeter/2
area=math.sqrt((s)*(s-ab)*(s-bc)*(s-ac))
angleA=math.acos((ab**2+ac**2-bc**2)/(2*ab*ac))*57.2957795131
angleB=math.acos((ab**2+bc**2-ac**2)/(2*ab*bc))*57.2957795131
angleC=math.acos((ac**2+bc**2-ab**2)/(2*ac*bc))*57.2957795131

print("=== Results ===")
print("Perimeter: "+str(perimeter))
print("Area: "+str(area))
print("AB: "+str(ab))
print("BC: "+str(bc))
print("AC: "+str(ac))
print("AB Midpoint: ("+str((ax+bx)/2)+", "+ str((ay+by)/2)+")")
print("BC Midpoint: ("+str((cx+bx)/2)+", "+ str((cy+by)/2)+")")
print("AC Midpoint: ("+str((ax+cx)/2)+", "+ str((ay+cy)/2)+")")
print(abfor)
print(acfor)
print(bcfor)
print("Angle A: "+str(angleA))
print("Angle B: "+str(angleB))
print("Angle C: "+str(angleC))
