from datetime import datetime
import math
now = (datetime.today().strftime('%Y-%m-%d'))
back_to_start = True

while back_to_start == True:

    with open('volumes.txt', 'a') as file_objet:
        
        w = int(input('Enter the width of the tire in mm (ex 205): '))
        a = int(input('Enter the aspect ratio of the tire (ex 60): '))
        d = int(input('Enter the diameter of the wheel in inches (ex 15): '))


        v = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)
        print()
        print(f'The approximate volume is {v:.2f} liters')

        approve_purchase = str(input('Do you want to purchase the tire with the specified dimensions? [Y/N]: '))
        approve_purchase = approve_purchase.lower()

        if approve_purchase == 'y':
            name = input('Enter the full name of the client: ')
            phone = input('Enter contact phone: ')
            adress = input('Enter delivery address: ')

            file_objet.write(f'{now}, {w}, {a}, {d}, {v:.2f} - Client Data: {name}, {phone}, {adress}\n')
            break
        
        elif approve_purchase == 'n':
            new_question = input('Do you want to make another query? [Y/N]: ')

            if new_question == 'y':
                back_to_start == True
            
            else:
                exit('Thank you for using our service')

"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use ),math.pi
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""