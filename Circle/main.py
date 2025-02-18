# main.py to calculate circumference & area of a circle - by Angelique Everitt

print()
print("This program calculates the circumference and area of a circle based on user input of radius.")
print()
import math
radius = float(input("Input the radius of the circle: "))
circumference = float(2*math.pi*radius)
area = float(math.pi*(radius*radius))
print("Given the radius ", radius, "the circumference is ", circumference)
print("Given the radius ", radius, "the area is ", area)
print()
print("fin")
print()
