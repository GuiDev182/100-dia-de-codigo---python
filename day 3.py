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

'''#pizza order project

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
            total_price = pepperoni_price_medium_large + large_pizza + price_extra_chesee'''


#prjrto treasure island

print('''                                                                    
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8 ''')

escolha = input("Bem vindo a ilha do tesouro \n Sua missão é achar o tesouro escondido. \n " \
"Você chegou em uma encruzilhada, voce tem duas opções, ir para a esquerda ou para a direita, o que voce escolhe? \n Digite 'esquerda' ou 'direita'\n R: ".lower)


if escolha == 'left':
    input("Você chegou em um lago grande, e no meio desse lago você avista uma pequena ilha no meio com varias arvores, Você tem duas opções: \n" \
    "você nada!\n você tenta procurar um bote \n Digite 'nadar ' ou 'bote' ")
        
    
else:
    print("Você anda para a direita e de repente passa em cima de varias folhas, e quando  menos percebe, você cai em um buraco grande." \
    "as folhas estavam escondendo o buraco. Você grita por ajuda, tenta sair, mais o buraco é muito gardne e escuro, e não tem ninguem na ilha\n" \
    " Anoitece, você esta com muita fome, o frio cortante deixa sua pele aspera, você escuta barulho de animais, tenta gritar por socorro mais uma vez mas ninguem te ouve\n" \
    "Você cai em sono!\n  Você acorda com um som de de alguem gritando: Vamos marujo, temos muita coisa para fazer!\n" \
    "Você levanta, e quando acaba de levantar, você vê uma silhueta de um homem com uma perna de pau, barbudo, com um gancho na mão e um chapéu de capitão \n" \
    " e ele te diz: vai ficar ai a vida toda?? ou melhor, vai ficar morto ai o tempo todo, hahaahahah!\n" \
    "e quando você olha para baixo, descobre que esta flutuando por cima de seu corpo, você se assusta e diz para si mesmo: Estou morto? O que aconteceu? \n" \
    " e o Capitão diz : Ta mais morto que esse papagaio no meu ombro ahahaah, agora vamos ao trabalho, temos muito mar pela frente, você morreu na milha ilha\n" \
    "e agora será meu escravo, você está preso a esta ilha eternamente, achou se quseria facil achar meu tesouro? MuaHaHaHa\n" \
    "Você aceita seu destino e começa a flutuar para junto ao capitão!!! \n" \
    "Ficou curioso para saber onde esta o tesouro?? Tente novamente!!!")





