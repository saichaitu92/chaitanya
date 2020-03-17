print ("length of triangle sides ")
x=float(input("x: "))
y=float(input("y: "))
z=float(input("z: "))
if x==y and y==z and x==z:
    print("equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("scalen triangle")

