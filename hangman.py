from random import choice
from sys import exit
def check_guessed():
    for x in word:
        if x in guessed:
            isGuessed = True
        else:
            isGuessed = False
            break
    return isGuessed
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
words = open("english.txt", encoding="UTF-8").read().split("\n") # источник 31 декабря 2023 года 17:26 по МСК (UTC+3) https://www.desiquintans.com/downloads/nounlist/nounlist.txt
words = words[4:] # отрезаем аббревиатуры
for i, word in enumerate(words):
    if not word.isalpha():
        del words[i] # оставляем только буквы
atts = 5
word = choice(words)
guessed = []
print(f"You have {atts} attempt" + "s." if atts > 1 else ".")
print("Attempts will decrease only if you enter wrong letter.")
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
            guessed.append(l)
    else:
        print("Wrong letter!")
        atts -= 1
    if check_guessed():
        print(word)
        break
else:
    print("You lost!")
    print(f"The word was: {word}")
    input("Press Enter to exit.")
    exit()
print("Congratulations! You won!")
input("Press Enter to exit.")
exit()