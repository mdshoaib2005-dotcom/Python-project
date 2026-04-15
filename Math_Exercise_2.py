#To calculate area of the circle

import math

radius = float(input("Enter the radius of the circle: "))
Area = math.pi* pow(radius,2)

print(f"The area of the circle of radius{radius} is {round(Area,4)}cm^2: ")