import math

item_number = int(input('Enter the number of items: '))
items_box = int(input('Enter the number of items per box: '))

packing = item_number/items_box

print(f'For {item_number} items, packing {items_box} items in each box, you will need {math.ceil(packing)} boxes.')