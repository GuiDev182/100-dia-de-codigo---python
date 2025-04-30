#pizza order exercise
'''
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_price_small = 2
pepperoni_price_medium_large = 3
price_extra_chesee = 1

print("Welcome to python pizza Deliveries!")
size = input("what size pizza do you want? S, M or L \n" + "R: ")
if size == 'S':
    total_price = small_pizza
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N \n" + "R: ")
    if pepperoni == 'Y':
        total_price = small_pizza + pepperoni_price_small
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = pepperoni_price_small + small_pizza + price_extra_chesee
    else:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = small_pizza + price_extra_chesee

elif size == 'M':
    total_price = medium_pizza
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N \n" + "R: ")
    if pepperoni == 'Y':
        total_price = medium_pizza + pepperoni_price_medium_large
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = pepperoni_price_medium_large+ medium_pizza + price_extra_chesee
    else:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = medium_pizza + price_extra_chesee

elif size == 'L':
    total_price = large_pizza
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N \n" + "R: ")
    if pepperoni == 'Y':
        total_price = large_pizza + pepperoni_price_medium_large
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = pepperoni_price_medium_large + large_pizza + price_extra_chesee
    else:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N \n" + "R: ")
        if extra_chesee == 'Y':
            total_price = large_pizza + price_extra_chesee
else:
    print("you typed the wrong inputs")
print(f"The total value is ${total_price}")'''

print('''*******************************************************************************
_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
input("Welcome to te Treasure Island \n Your mission is to find the treasure \n You're at a cross road. Where do you want to go?")



