#To calculate the hypoteneous of an right angled triangle
import math
a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C= {round(c, 5)} : ")
