import math
manufacterd_items = int(input("Enter number of manufactured items "))
items_per_box = int(input("Enter the number of items that will be packed per box "))
boxes = math.ceil(manufacterd_items / items_per_box)
print(f"you will need {boxes: .2f} boxes")