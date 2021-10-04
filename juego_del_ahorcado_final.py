import os
import random
from random import choice


DATA = []
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for word in f:
        DATA.append(word.strip())


random_word = choice(DATA)
enumerate_word = {}
hidden_word = []
found_word_list = []

for i in range(len(random_word)):
    found_word_list.append('_')

for num, letter in enumerate(random_word):
    enumerate_word.update({num: letter})

for letter in random_word:
    hidden_word.append(letter)


def run():
    while found_word_list != hidden_word:
        os.system("clear")
        print('¡Adivina la palabra!')
        found_word = ' '.join(found_word_list)
        print(found_word)
        print('\n')
        chosen_letter = input('Ingresa una letra: ')
        for num, letter in enumerate_word.items():
            if chosen_letter == letter:
                found_word_list[num] = letter
    os.system("clear")
    print(f'¡Ganaste! La palabra era {random_word}')
    

if __name__ == "__main__":
    run()