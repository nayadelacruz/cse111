#importing modules
import math

#Request values from user
w = float(input("Enter the width of the tire in mm "))
a = float(input("Enter the aspect ratio of the tire "))
d = float(input("Enter the diameter of the wheel in inches "))

#Funtion
volume = round(((math.pi *(w **2) * a) * ((w * a) + (2540 * d)))/ 10000000000,2)

#Print volume of a tire
print(f"The aproximate volumne is {volume: .2f} liters")

#print current time
from datetime import datetime 
current_day = datetime.now()
print(f"{current_day: %Y-%m-%d}")

#open tx file
with open("text_volume.txt", "at") as text_file:
    #print tire information and date in the text file
    print(f"{current_day: %Y-%m-%d}, {w}, {a}, {d}, {volume}", file=text_file)

#asking custumer if wants to buy tires
question_tires = input("Do you want to buy tires with the provided dimensions? ") 
if question_tires == "yes":
    phone_number = input("Enter your phone number without spaces or dashes ")
    with open("text_volume.txt", "at") as text_file:
        print(f"phone number {phone_number}", file=text_file)
