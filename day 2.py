print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? " + "$"))
tip_give = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

each_person_pay = (total_bill / people_to_split) * (tip_give / 100 + 1)


print(f"Each person should pay: ${each_person_pay:.2f}")