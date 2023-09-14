from datetime import datetime
#values
discount_rate = .10
tax_rate = .06
subtotal = float(input("Enter Subtotal "))
currentDate = datetime.now()
day_of_the_week = currentDate.weekday()
#function
if subtotal >= 50 and (day_of_the_week == 1 or day_of_the_week == 2):
    discount = round(subtotal * discount_rate, 2)
    subtotal -= discount
    print(f"Discount is ${discount: .2f}")

tax = round(subtotal * tax_rate, 2)
print(f"Tax rate is ${tax: .2f}")  

total = round(subtotal + tax, 2)
print(f"Your total is ${total: .2f}")


 