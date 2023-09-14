#importing modules
import math
#Request values from user
w = float(input("Enter the width of the tire in mm "))
a = float(input("Enter the aspect ratio of the tire "))
d = float(input("Enter the diameter of the wheel in inches "))
#Funtion
volume = ((math.pi *(w **2) * a) * ((w * a) + (2540 * d)))/ 10000000000
#Print volume of a tire
print(f"The aproximate volumne is {volume: .2f} liters")