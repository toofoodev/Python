# Guess The Number | 16 Lines
# Made by Wes
# If you edit or share this script, please give credits!
# For more scripts, go to: https://github.com/toofoodev/Python

import random

numlist = list(range(1, 10))
numlh = list(range(1, 4))
guessnum = random.choice(numlist)

def play():
    print(guessnum)
    guessin = input("Guess: ")
    if int(guessin) == guessnum:
        print("You guessed right!")
    else:
        hin = random.choice(numlh)
        hints1 = guessnum + hin
        hint = hints1 * 2
        print(f"Hint: {hint}")
        play()
play()
