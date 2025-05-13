#Step 1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called palavra_forca.
#TODO-2 - Ask the user to letra_escolhida a letter and assign their answer to a variable called letra_escolhida. Make letra_escolhida lowercase.
#TODO-3 - Check if the letter the user letra_escolhidaed (letra_escolhida) is one of the letters in the palavra_forca. print "Right" for correct
# and "wrong" if it's not

#Step 2
#TODO-1: - Create an empty List called display.
#For each letter in the palavra_forca, add a "_" to 'display'.
#So if the palavra_forca was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to letra_escolhida.
#TODO-2: - Loop through each position in the palavra_forca;
#If the letter at that position matches 'letra_escolhida' then reveal that letter in the display at that position.
#e.g. If the user letra_escolhidaed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#step 3
#TODO-1: - Use a while loop to let the user letra_escolhida again. The loop should only stop once the user has letra_escolhidaed all the letters in the palavra_forca and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
#TODO-2: Change the for loop so that you keep the previous correct letter


import random

lista_palavras = ["aardvark", "baboon", "camel"]


palavra_forca= random.choice(lista_palavras)
print(palavra_forca)
lista_palavra_forca = []
letra_escolhida = input("letra_escolhida a letter: \n R: ").lower()
for cada_letra in palavra_forca:
    if letra_escolhida == cada_letra:
        lista_palavra_forca.append(letra_escolhida)
    else:
        lista_palavra_forca.append("_")
contador_palavra = 0
while contador_palavra != len(palavra_forca):
    letra_escolhida = input("letra_escolhida a letter: \n R: ").lower()
    for cada_letra in lista_palavra_forca:
        if letra_escolhida == cada_letra:
            lista_palavra_forca.remove('_')
            lista_palavra_forca.append(letra_escolhida)
        contador_palavra += 1
    else:
        lista_palavra_forca.append('_')






