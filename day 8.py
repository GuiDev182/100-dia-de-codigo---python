#function with inputs


'''def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet('guilherme')

#function with more than 1 input

def greet_with_more_parameters(name, location):
    print(f"Hi {name}")
    print(f"what isd it like in {location}")
greet_with_more_parameters('guilherme', 'divinopolis')'''
from rsa import encrypt

#challenge

'''Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 
L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 
Love Score = 53
Example Input 

calculate_love_score("Kanye West", "Kim Kardashian")

Example Output

42

def calculate_love_score(name1, name2):
    word_true = ['t','r','u','e']
    love = ['l','o','v','e']

    score_name1 = 0
    score_name2 = 0
    total_score = 0

    for letter in name1:
        if letter in word_true:
            score_name1 += 1
        if letter in love:
            score_name2 += 1

    for letter in name2:
        if letter in word_true:
            score_name1 += 1
        if letter in love:
            score_name2 += 1

    total_score = str(score_name1) + str(score_name2)
    print(f"Your love score is {total_score}")


calculate_love_score("Angela Yu", "Jack Bauer")'''

logo = """                                                                                                                                     
  ,ad8888ba,                                                         
 d8"'    `"8b                                                        
d8'                                                                  
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88  
  
  ,ad8888ba,  88             88                                 
 d8"'    `"8b ""             88                                 
d8'                          88                                 
88            88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           88 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                 88                                             
                 88                                                                          
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


def caesar(original_text, shift_amount,
           operation_direction):
    final_text_list = []

    for letter in original_text:
        if letter not in alphabet:
            final_text_list.append(letter)
        else:
            current_index = alphabet.index(letter)

            # Ajusta o shift para decodificação
            if operation_direction == 'decode':
                shift_amount *= -1

            # Calcula o novo índice, lidando com o "enrolamento" do alfabeto
            new_index = (current_index + shift_amount) % len(alphabet)

            final_text_list.append(alphabet[new_index])

    # Junta a lista de caracteres em uma string APÓS o loop
    processed_message = "".join(final_text_list)

    return processed_message  # Retorna a string processada


# Chama a função e armazena o resultado
result_message = caesar(text, shift, direction)

# Imprime o resultado fora da função
print(f"Here is the {direction} result: {result_message}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(text, shift, direction)

    restart = input("type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == 'no':
        should_continue = False
        print("GoodBye")

