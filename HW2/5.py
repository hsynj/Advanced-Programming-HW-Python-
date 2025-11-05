import random
import os

COLORS = ['W', 'B', 'R', 'Y', 'P', 'G', 'D', 'O']
COLOR_NAMES = {
    'W': 'White', 'B': 'Blue', 'R': 'Red', 'Y': 'Yellow',
    'P': 'Purple', 'G': 'Green', 'D': 'Dark', 'O': 'Orange'
}
CODE_LENGTH = 4

def calculate_score(code, guess):

    black_pins = 0
    white_pins = 0

    code_c = list(code)
    guess_c = list(guess)

    for i in range(CODE_LENGTH):
        if guess[i] == code[i]:
            black_pins += 1
            code_c[i] = 0
            guess_c[i] = 0

    for i in range(CODE_LENGTH):
        if guess_c[i] != 0 and guess_c[i] in code_c:
            white_pins += 1
            code_c[code_c.index(guess_c[i])] = 0

    return black_pins, white_pins


def show_color():
    print("Colors: ")
    for color in COLOR_NAMES:
        print(f"{color} : {COLOR_NAMES[color]}")


def cls():
    os.system('cls')


# sample for dont repeat
code = random.sample(COLORS, CODE_LENGTH)

cls()
print("MASTERMIND GAME")
print("We selected a 4 different color.")
print("You need to guess it within 8 moves.")
print("Black pin: correct color and position")
print("White pin: correct color only")
print("Enter 'q' for quit game")
print(code)
show_color()
tries = 0
while True:
    entry = input(" Please enter your entry: ").upper()
    if entry == 'Q':
        print(f"Game Over\nThe secret code was: {code}")
        break
    if len(entry) != CODE_LENGTH or not all(color in COLORS for color in entry):
        print("Please enter a valid 4-letter code using the colors above.")
        continue
    tries += 1
    score = calculate_score(code, entry)
    if score[0] == CODE_LENGTH:
        print("======> Congratulations! You won!")
        break
    elif tries >= 8:
        print(f"OHHHH NOOO, you lost! The secret code was '{code}'.")
        break
    else:
        print(f"Guess {tries}/8: {score[0]} black pins and {score[1]} white pins")

print("\nTo play again, restart the program.")
