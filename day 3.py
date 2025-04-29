#pizza order project

small_pizza = 15
medium_pizza = 20
large_pizza = 25
total_price = 0
pepperoni_price_small = 2
pepperoni_price_medium_large = 3
price_extra_chesee = 1

print("Welcome to python pizza Deliveries!")
size = input("what size pizza do you want? S, M or L \n" + "R: ").lower
if size == 's':
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N").lower
    if pepperoni is True:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N").lower
        if extra_chesee is True:
            total_price = pepperoni_price_small + small_pizza + price_extra_chesee             
elif size == 'm':
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N").lower
    if pepperoni is True:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N").lower
        if extra_chesee is True:
            total_price = pepperoni_price_medium_large + medium_pizza + price_extra_chesee
elif size == 'l':
    pepperoni = input("Do you want pepperoni on your pizza? \n" + "Y or N").lower
    if pepperoni is True:
        extra_chesee = input("Do you want extra cheese on your pizza? \n" + "Y or N").lower
        if extra_chesee is True:
            total_price = pepperoni_price_medium_large + large_pizza + price_extra_chesee
