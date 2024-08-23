import random
import os
import time


def chooseNumber():
    os.system("cls")

    number = random.randint(1, 10)

    guess = input("Choose a number between 1-10: ")

    if guess == "break":
        exit()

    try:
        guess = int(guess)
    except ValueError:
        print("Choose only between 1-10!")
        time.sleep(1)
        os.system("cls")
        chooseNumber()

    if guess < 0 or guess > 10:
        print("Choose only between 1-10!")
        time.sleep(1)
        os.system("cls")
        chooseNumber()

    if guess == number:
        print("You win")
        time.sleep(1)
        print("Try again?")

        while True:
            choose = input("(1)Yes\n(2)No ")

            try:
                choose = int(choose)
            except ValueError:
                os.system("cls")
                print("Choose only between 1 and 2!")
                time.sleep(1)
                os.system("cls")
                continue

            if choose == 1:
                os.system("cls")
                chooseNumber()

            elif choose == 2:
                exit()

            else:
                os.system("cls")
                print("Choose only between 1 and 2!")
                time.sleep(1)
                os.system("cls")
                continue

    else:
        print("You Lose!")
        time.sleep(1)
        os.system("cls")
        print("The Correct Answer was..." + str(number))
        time.sleep(1)
        print("Try again?")

        while True:

            choose = input("(1)Yes\n(2)No ")

            try:
                choose = int(choose)
            except ValueError:
                os.system("cls")
                print("Choose only between 1 and 2!")
                time.sleep(1)
                os.system("cls")
                continue

            if choose == 1:
                os.system("cls")
                chooseNumber()

            elif choose == 2:
                exit()

            else:
                os.system("cls")
                print("Choose only between 1 and 2!")
                time.sleep(1)
                os.system("cls")
                continue


chooseNumber()
