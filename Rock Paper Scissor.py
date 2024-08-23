import random
import time
import os


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def RockPaperScissors():
    clearScreen()

    elements = ["Rock", "Paper", "Scissors"]
    enemy = random.choice(elements)

    print("Rock Paper Scissor Game!")
    guess = input("(1)Rock\n(2)Paper\n(3)Scissors\n").lower()

    if guess == "rock" or guess == "1":
        guess = "Rock"

    elif guess == "paper" or guess == "2":
        guess = "Paper"

    elif guess == "scissors" or guess == "3" or guess == "scissor":
        guess = "Scissors"

    else:
        clearScreen()
        print("Choose Only!\n(1)Rock\n(2)Paper\n(3)Scissors\n")
        time.sleep(1)
        return main()

    os.system("cls")
    print("ROCK")
    time.sleep(.5)
    os.system("cls")
    print("PAPER")
    time.sleep(.5)
    os.system("cls")
    print("SCISSORS")
    time.sleep(1)
    os.system("cls")

    print("Bot: " + str(enemy).capitalize())
    print("You: " + str(guess).capitalize())

    if enemy == guess:
        print("TIE")

    elif (enemy == "Rock" and guess == "Paper" or enemy == "Paper" and guess == "Scissors"
          or enemy == "Scissors" and guess == "Rock"):
        print("You Win")

    else:
        print("You lose")


def main():
    clearScreen()
    RockPaperScissors()

    while True:
        try_again = input("Play again? (y/n)")
        if try_again.isalpha() or try_again == "":
            if try_again == "" or try_again == "y":
                clearScreen()
                main()
            elif try_again == "n":
                clearScreen()
                exit()
            else:
                print("Invalid Input!")

        else:
            print("Invalid Input!")


if __name__ == '__main__':
    main()
