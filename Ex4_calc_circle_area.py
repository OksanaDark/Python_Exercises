#circle_radius = float(input("Write circle radius"))

#circle_area = 3.14 * (circle_radius * circle_radius)

#print(circle_area)

from math import pi

radius = float(input("Circle radius is: "))

print(f"Area circle with the radius {radius} is " + str(pi * (radius ** 2)))
