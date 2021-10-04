import os
import random
from random import choice


DATA = []
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for word in f:
        DATA.append(word.strip())

random_word = choice(DATA).upper()

enumerate_word = {num: letter for num, letter in enumerate(random_word)}
found_word_list = ['_' for i in range(len(random_word))]
hidden_word = [letter for letter in random_word]


def run():
    while found_word_list != hidden_word:
        os.system("clear")
        print('¡Adivina la palabra!')
        found_word = ' '.join(found_word_list)
        print(found_word + '\n')
        chosen_letter = input('Ingresa una letra: ')
        assert chosen_letter.isalpha(), "Solo puedes ingresar letras"
        for num, letter in enumerate_word.items():
            if chosen_letter.upper() == letter:
                found_word_list[num] = letter
    os.system("clear")
    print(f'¡Ganaste! La palabra era {random_word}')
    

if __name__ == "__main__":
    run()