'''#exercicio - quem irá pagar?
import random

amigos = ["joao", "maria", "jose", "ciclano"]

quem_ira_pagar = random.choice(amigos)

print(f"Quem irá pagar a conta hoje é : {quem_ira_pagar}")'''
import random

#rock, paper, scissor project


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___ '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


print("Welcome to the rock, paper and scissors game!")
you_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n R: "))
random_choice = [rock, paper, scissors]
pc_choice = random.randint(0,2)

if you_choice == pc_choice:
    print(rock)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("it's a Draw!")
elif you_choice == 0 and pc_choice == 1:
    print(rock)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("Computer wins!!!")
elif you_choice == 0 and pc_choice == 2:
    print(rock)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("You win!")
elif you_choice == 1 and pc_choice == 0:
    print(paper)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("You win!")
elif you_choice == pc_choice:
    print(paper)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("It's a Draw!")
elif you_choice == 1 and pc_choice == 2:
    print(paper)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("Computer wins!")
elif you_choice == 2 and pc_choice == 0:
    print(scissors)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("Computer Wins!")
elif you_choice == 2 and pc_choice == 1:
    print(scissors)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("You Win!")
elif you_choice == pc_choice:
    print(scissors)
    print("computer chose:")
    print(f"{random_choice[pc_choice]}")
    print("It's a Draw!")
else:
    print("wrong answer, try again!")