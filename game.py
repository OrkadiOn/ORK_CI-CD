import random
import sys

def guess_number():
    number = random.randint(1, 10)
    try:
        guess = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Введите число от 1 до 10 как аргумент командной строки.")
        sys.exit(1)

    if guess == number:
        print("Угадал!")
    else:
        print(f"Не угадал. Было число: {number}")

guess_number()
