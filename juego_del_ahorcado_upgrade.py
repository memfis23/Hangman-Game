import os
import random


HANGMAN_TITLE = '''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
'''

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

def score(attemps):
    point = 100 / 6
    final_score = point * attemps
    return print(f'Tu puntuacion es: {round(final_score)}/100')

def end_game(result, word, attemps):
    os.system("clear")
    print(f'{result} La palabra era {word}')
    score(attemps)

def run():
    data = read()
    word = normalize(random.choice(data))
    hidden_word_underscords = ["_"] * len(word)
    hidden_word_list = [letter for letter in word]
    attemps = 6
    score = 100

    while True:
        os.system("clear")
        print(HANGMAN_TITLE)
        print('¡Adivina la palabra!')
        hidden_word = ' '.join(hidden_word_underscords)
        print(hidden_word + '\n')
        print(IMAGES[attemps])
        print(f"intentos: {attemps}")
        print(f'puntaje: {round(score)}' + '\n')
        chosen_letter = input("Elige una letra: ").strip().upper()
        assert chosen_letter.isalpha(), "Solo puedes ingresar letras"

        found = False
        for idx, letter in enumerate(word):
            if letter == chosen_letter:
                hidden_word_underscords[idx] = chosen_letter
                found = True

        if not found:
            attemps -= 1
            score -= 100 / 6 

        if hidden_word_underscords == hidden_word_list:
            end_game('¡Ganaste! 😎', word, attemps)
            break

        if attemps == 0:
            end_game('¡Perdiste! 😢', word, attemps)
            break


if __name__ == "__main__":
    run()