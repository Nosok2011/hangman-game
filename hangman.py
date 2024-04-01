from random import choice
from sys import exit
def check_guessed(g, w):
    for x in w:
        if x in g:
            isGuessed = True
        else:
            isGuessed = False
            break
    return isGuessed
def play_again():
    again = input("Do you want to play again? (y/n) ")
    match again:
        case "y":
            play()
        case "n":
            exit()
        case _:
            print("Incorrect choice!")
            play_again()
def play():
    word = choice(words)
    atts = len(word) if len(word) > 5 else 5
    guessed = []
    wrong = []
    print(f"You have {atts} attempts.")
    print("Attempts will decrease only if you enter wrong letter and it wasn't entered before.")
    print("If you enter more than 1 letter, only 1st letter will be used.")
    print("Let's start!")
    print("Letters in the word:", len(word))
    while not atts == 0:
        s = "s" if atts > 1 else ""
        print(f"You have {atts} attempt{s} left.")
        for l in word:
            if l in guessed:
                print(l, end="")
            else:
                print("_", end="")
        print()
        l = input("Enter letter: ")
        if not l.isalpha():
            print("Input must be a letter!")
            continue
        else:
            l = l[0].lower()
        if l in word:
            if l in guessed:
                print("This letter is already guessed!")
            else:
                print("Correct!")
                guessed.append(l)
        else:
            print("Wrong letter!")
            if l not in wrong:
                atts -= 1
                wrong.append(l)
            else:
                print("(attempts weren't decreased)")
        if check_guessed(guessed, word):
            print(word)
            break
    else:
        print("You lost!")
        print(f"The word was: {word}")
        play_again()
    print("Congratulations! You won!")
words = open("english.txt", encoding="UTF-8").read().split("\n") # источник 31 декабря 2023 года 17:26 по МСК (UTC+3) https://www.desiquintans.com/downloads/nounlist/nounlist.txt
for i, word in enumerate(words):
    if not word.isalpha():
        del words[i] # оставляем только буквы
print("(sorry for my english if it's bad, i'm a 12 year kid from russia)")
print("(but sometimes i search some translations in the internet, hehe)")
print("Hello, welcome to Hangman!")
while True:
    print("Choose action:")
    print("1. Play")
    print("2. Exit")
    try:
        act = int(input())
    except ValueError:
        print("Input must be a number!")
        continue
    match act:
        case 1:
            break
        case 2:
            exit()
        case _:
            print("Wrong choice!")
play()
play_again()
