import random

def guess_number():
    number = random.randint(1, 10)
    print("Я загадал число от 1 до 10. Попробуй угадать!")
    while True:
        guess = int(input("Твой вариант: "))
        if guess == number:
            print("Поздравляю! Ты угадал!")
            break
        elif guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

if __name__ == "__main__":
    guess_number()


