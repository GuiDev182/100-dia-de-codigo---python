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

escolha01 = input("Bem vindo a ilha do tesouro \n Sua missão é achar o tesouro escondido. \n " \
"Você chegou em uma encruzilhada, voce tem duas opções, ir para a esquerda ou para a direita, o que voce escolhe? \n Digite 'esquerda' ou 'direita'\n R: ").lower()


if escolha01 == 'esquerda':
    escolha02 = input("Você chegou em um lago grande, e no meio desse lago você avista uma pequena ilha no meio com varias arvores, Você tem duas opções: \n" \
    "você nada, ou espera por um bote \n Digite 'nadar ' ou 'bote' \n R:").lower()
    if escolha02 == 'esperar':
        escolha03 = input("Você espera um pouco e descobre que tem um bote mais a esquerda e entra nele, você chega na ilha, sai do bote e quando você sai do boate e dá três passos\n \
                           você escuta um estrondo atras e você e vê um tentáculo enorme destruindo o bote, você fica assustado e você vê que o tentaculo começa a submergir de volta para o lago\
                           Você pensa: como irei voltar novamente? Meu bote foi destruido, e tem uma criatura enorme no lago \
                           então você continua a caminhar para frente da ilha, você avista uma casa bem no meio da ilha e resolve ir até lá bem devagar \
                           você puxa a maçaneta da porta bem devagar e descobre que tem uma parede com três portas, uma com cada cor diferente. \
                           Uma porta com a cor VERMELHA \
                           Uma porta com a cor AMARELA \
                           Uma porta com a cor AZUL \
                           Você pensa em qual cor escolher, pois não sabe o que tem atrás de cada porta \
                           Qual será sua escolha?? \
                           R:").lower()
        if escolha03 == "vermelha":
            print("você escolheu a porta vermelha. e quando menos espera você entra em uma sala escura,e de repente começa um fogo intenso.\n \
                   Sem saída você começa a gritar por socorro, porem as chamas começam a ficar mais forte e densas, um calor infernal começa a tomar conta de você \
                   você entra em desespero e vê que nao tem outra saida a nao ser esperar a morte, brutalmente você é consumido pelas chamas. \
                  Ficou curioso para saber onde esta o tesouro?? Tente novamente!!!")
        elif escolha03 == "amarela":
            print("você abre a porta e quando você menos espera, uma luz bem forte te cgea por uns instantes, e quando você olha para frente, vocÊ se espanta! \n \
            uma sala cheia de tesouros, moedas, objetos de grande valor, você fica maravilhado com a quantidade enorme de tesouro e pensa: - Estou rico! \
            você pula de alegria, e fica admirando todo aquel tesouro dourado! \
            porém você pensa em uma coisa: - Como vou retirar todo aquele tesouro dali ? Meu bote foi destruido, e existe uma criatura naquele lago! \
            E agora? como você irá carregar todo esse tesouro? você está rico, mas afinal, não adianta ser rico, e não conseguir gastar um centavo do tesouro \
            Bom...o que você fará, ficara para uma outra historia! Fim do jogo")
        elif escolha03 == "azul":
            print("Você abre a porta, e vê uam sala com pouca iluminação, algumas pilastras e um carpete vermelho indo da porta até o final da sala \n \
             você começa a caminhar, e vê que as pilastras tem alguns sulcos enormes, você decide averiguar e quando chega mais perto, você descobre que são marcas de garras enormes \
             você se assusta e tenta voltar, porém a porta esta trancada e você nao consegue abrir. \
             você escuta um grunhido enorme vindo do fundo da sala, e quando você menos espera, grandes olhos vermelhos aparecem no fundo da sala, e a cada vez chegando mais perto \
             de repente você vê um enorme lobo, com garras afiadas e uma boca enorme com dentes afiados, e ele começa a te perseguir, você tenta correr e se desvencilhar dele \
             Você tenta correr porém ele te prende com suas garras, e quando você menos espera, ele solta um urro estridente, que faz você desmaiar! \
             Alguns minutos depois, você acorda com muita dor, e você percebe que não consegue fazer nenhum movimento, e quando vocÊ olha para baixo, você vê seu corpo imovel no chao \
             e descobre que você está preso em algum tipo de quadro, e perceeb tambem que há outros quadros ao seu lado, com outras pessoas presas a ele, você tenta pedir socorro \
             porém o prisioneiro ao seu lado diz : - não há como escapar, estou preso aqui a mais de 10 anos e nunca consegui sair, os outros estão presos aqui a mais tempo que eu, não há o que fazer \
             você senta e pensa se existe alguma forma de sair daquele lugar, porem você não consegue movimentar da cabeça para baixo e não a nada que possa fazer \
             Ficou curioso para saber onde esta o tesouro?? Tente novamente!!!")
        else:
            print("Você não escolheu sabiamente nenhuma das portas, achou que podia me enganar?? Eu, o grande narrador! \n \
              por isso, te lançarei no limbo do esquecimento dos erros, onde você ficará lá eternamente até tentar novamente Muahahahaha \n \
               Fim de jogo")
    else:
        print("Você decide que consegue nadar até o meio da ilha, e começa a nadar, quando você chega a metade do caminho, você avista algo no lago que parece suspeito \n \
              e está vindo em sua direção, você consegue olhar mais de longe e vê que em sua direção vem uma criatura monstruosa com seis tentáculos, você fica desesperado \
              e tenta a todo custo voltar para a beira de onde você estava, você olha pra trás e vê que a cada momento a criatura chega mais perto, e você grita por socorro \
              você começar perder as forças, a adrenalina começa a ficar mais intensa, seu coração bate mais forte, e a criatura vai chegando mais perto, você começa a sentir \
              uma sensação estranha, como se algo estivesse saindo do seu corpo, e você começa a olhar em volta do seu corpo e percebe que voce aparenta estar saindo do corpo \
              você começa a ficar fraco, sua cabeça fica zonza, e você apaga por um momento! Quando você acorda, você está de frente para a criatura, no qual está freneticamente a te olhar, \
              você se assusta pois é um polvo gigante, uma criatura imensa, 10x maior que você, você percebe que esta no meio do mar sengo segurado por um de seus tentáculos \
              voce tenta se desvencilhar dos tentáculos, quando você olha para o lado, você vê seu corpo descendo rio abaixo para o lago, e aí você descobre que você na verdade \
              ja está morto. A criatura olha para você com seus olhos vermelhos e diz: - Meu nome é NerseLake, reis dos lagos! Como ousa atravessar o meu rio sem minha permissão! \
              Seus castigo será ser meu prisioneiro até a eternidade! \
              E a criatura começa a submergir e te puxa junto com ela, e vocês somem em meio a escuridão do lago! Ficou curioso para saber onde esta o tesouro?? Tente novamente!!!")

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





