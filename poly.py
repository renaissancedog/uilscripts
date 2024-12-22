import math

n=int(input("Enter number of sides: "))
array = [[0, 0] for i in range(n)]
print("Enter points either clockwise or anticlockwise.")
for i in range(n):
  x=int(input("Point "+str(i+1)+" X: "))
  y=int(input("Point "+str(i+1)+" Y: "))
  array[i][0]=x
  array[i][1]=y
area=0
perimeter=0
for i in range(n):
  if (i!=n-1):
    perimeter+=math.sqrt((array[i][0]-array[i+1][0])**2+(array[i][1]-array[i+1][1])**2)
    area+=array[i][0]*array[i+1][1]
    area-=array[i][1]*array[i+1][0]
  else:
    perimeter+=math.sqrt((array[i][0]-array[0][0])**2+(array[i][1]-array[0][1])**2)
    area+=array[n-1][0]*array[0][1]
    area-=array[n-1][1]*array[0][0]
area=abs(area/2)
print("=== Results ===")
print("Perimeter: "+str(perimeter))
print("Area: "+str(area))