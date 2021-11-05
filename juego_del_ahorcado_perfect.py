import os
import random


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read()
    random_word = random.choice(data)
    # enumerate_word = {num: letter for num, letter in enumerate(random_word)}
    found_word_list = ["_"] * len(random_word)
    hidden_word = [letter for letter in random_word]

    while found_word_list != hidden_word:
        os.system("clear")
        print('¡Adivina la palabra!')
        found_word = ' '.join(found_word_list)
        print(found_word + '\n')
        chosen_letter = input('Ingresa una letra: ').strip().upper()
        assert chosen_letter.isalpha(), "Solo puedes ingresar letras"
        for num, letter in enumerate(random_word):
            if chosen_letter == letter:
                found_word_list[num] = letter
    os.system("clear")
    print(f'¡Ganaste! La palabra era {random_word}')
    

if __name__ == "__main__":
    run()