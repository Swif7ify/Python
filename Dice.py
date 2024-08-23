import os
import random


def main():
    while True:
        clear_screen()
        choice = input("(1) Roll a dice\n(2) Roll 2 dice\n")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 2:
                if choice == 1:
                    clear_screen()
                    rolling_one_dice()
                else:
                    clear_screen()
                    rolling_two_dice()
                break
            else:
                print("Please enter a number between 1 and 2.")
        else:
            print("Please enter a number")


def rolling_two_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")


def rolling_one_dice():
    dice1 = random.randint(1, 6)
    print(f"Dice 1: {dice1}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
