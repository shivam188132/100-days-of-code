from hangmanword import word_list
from hangmanart import stages,logo
import random
is_on = True


print(logo)
random_word = random.choice(word_list)
life =  len(random_word)
print(life)
print(random_word)
random_word_list = [char for char in random_word]
print(random_word_list)

empty_blank = ["_" for char in random_word]
print(empty_blank)

while is_on:

    guessed_alphabet = input("Please enter your guess: \n").lower()

    # guessed_alphabet_list = [char for char in guessed_alphabet]
    

    for word in random_word_list:
        if guessed_alphabet == word:
            word_position = random_word_list.index(guessed_alphabet)
            empty_blank[word_position] = word
            print(empty_blank)
