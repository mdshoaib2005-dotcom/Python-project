#Calculate teh circumference of the circle

import math
radius = float(input("Enter the radius of circle:"))
circumference  = 2* math.pi* radius

print(f"The circumference of the circle of r={radius} is {round(circumference, 5)}cm")



#round(number, n digits) so here output will be given upto n place after decimal