import os
import random
from random import choice


def splitString(chain):
    cifra = ""
    contador = 0
    for numero in chain:
        if contador == 1:
            cifra += ' '
            contador = 0

        contador += 1
        cifra += numero

    return cifra


def prueba(word):
    for letter in word:
        return letter.replace(letter, '_')


DATA = []
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for word in f:
        DATA.append(word.strip())

# enumerated_data = {}
# for num, word in enumerate(DATA, 1):
#     enumerated_data.update({num: word})

# random_word = enumerated_data[random.randint(1, 171)]

random_word = choice(DATA)
separate_word = {}
hidden_word = splitString(random_word)

list_word = []
for letter in random_word:
    list_word.append(letter)

for num, letter in enumerate(random_word):
    separate_word.update({num: letter})
    

def run():
    found_word = []
    
    os.system("clear")
    print('¡Adivina la palabra!')
    
    # for letter in separate_word.values():
    #     print(letter.replace(letter, '_'), end = ' ')
    for letter in hidden_word:
        print(letter.replace(letter, '_'), end = ' ')
    # print('_ ' * len(random_word))
    print('\n\n')
    chosen_letter = input('Ingresa una letra: ')

    while found_word != list_word:
        os.system("clear")
        print('¡Adivina la palabra!')
        word = '_ ' * len(random_word)
        
        break



if __name__ == "__main__":
    run()