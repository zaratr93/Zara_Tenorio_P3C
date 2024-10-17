import math
import datetime
import os

today = datetime.datetime.now().date()
proceed = 'do not pass'

def whole_check(variable):
    while True:
        try:
            return int(variable)
        except:
            variable = input('\033[91mPlease enter a WHOLE number\033[0m\nInput: ')

w = whole_check(input('Enter the width of the tire in mm\nInput: '))
a = whole_check(input('Enter the aspect ratio of the tire\nInput: '))
d = whole_check(input('What is the diameter of the wheel in inches\nInput: '))

awnser = (((float(math.pi) * (int(w) ** 2)) * (int(a) * ((int(w) * int(a)) + (2540 * int(d)))))/10000000000)
print('\nThe aproximate value is:',round(awnser, 2),'Liters')
tire_cost = (100/40) * awnser
while True:
    tire_buy = input(f"\nThe approximate value of a {w}/{a}R{d} tire is: ${round(tire_cost, 2)} a tire\nWould you like to purchase a tire of this size? (y,n)\nInput: ")
    if tire_buy in ['y', 'Y', 'y ', 'Y ']:
        proceed = 'pass'
        phone_number = input('Would you please provide us with your phone number?\nInput: ')
        verify_phone_number = input(f"Is this your phone number?: {phone_number} (y,n)\nInput: ")
        while verify_phone_number not in ['y', 'Y', 'y ', 'Y ', 'n', 'N', 'n ', 'N ']:
            verify_phone_number = input(f"\n\033[91mPlease enter a valid input...\033[0m\nIs this your phone number?: {phone_number} (y,n)\nInput: ")
        if verify_phone_number in ['n', 'N', 'n ', 'N ']:
            phone_number = input("Re-enter yout phone number\nInput: ")
            break
        else:
            break
    if tire_buy in ['n', 'N', 'n ', 'N ']:
        print('No purchase request has been made')
        break
    else:
        print('\n\033[91mplease enter a valid input\033[0m')
with open('volumes.txt', 'a') as file:
    file.write(f"\n{today}\nThe width of the tire is: {w}\nThe Aspect ratio of the tire is: {a}\nThe diameter of the wheel is: {d}\nThe approximate liter size is: {round(awnser, 2)} Liters")
    if proceed == 'pass':
        file.write(f"\nYour phone number: {phone_number}    Cost of tire: ${round(tire_cost, 2)}\n{w},{a},{d},{round(awnser, 2)}")
    else:
        file.write(f"\n{w},{a},{d},{round(awnser, 2)}")
print("The file was created at:", os.getcwd())
file_path = 'volumes.txt'
os.startfile(file_path)