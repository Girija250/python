import math
def peri_circle(r):
    peri2=float(2*3.14*r);
    print("Perimter of circle is:",peri2)
def peri_triangle(a,b):
    hypotenuse=float(math.sqrt(a*a+b*b))
    peri3=float(a+b+hypotenuse)
    print("Perimter of right angled triangle is:",peri3)
def peri_rectangle(a,b):
    peri4=float(2*(a+b))
    print("Perimter of rectangle is:",peri4)

radius=float(input("enter the radius of circle:"))
peri_circle(radius)

length=float(input("enter the length of rectangle:"))
breadth=float(input("enter the breadth of rectangle:"))
peri_rectangle(length,breadth)

base=float(input("enter the base of right angled triangle:"))
height=float(input("enter the height of right angled triangle:"))
peri_triangle(base,height)
