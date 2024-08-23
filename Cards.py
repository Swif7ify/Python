import random
import time
import os


def clearScreen():
    os.system("cls")


def main():
    print("Welcome To Cards\n")
    time.sleep(1)
    choice = input("(1)Choose a Card\n(2)See all the Cards\n(3)Randomize Deck\n")

    try:
        choice = int(choice)
    except ValueError:
        clearScreen()
        print("Choose Only 1-3")
        time.sleep(1)
        clearScreen()
        main()

    if choice < 1 or choice > 3:
        clearScreen()
        print("Choose Only 1-3")
        time.sleep(1)
        clearScreen()
        main()

    if choice == 1:
        clearScreen()
        chooseCard()

    elif choice == 2:
        clearScreen()
        allCards()

    else:
        clearScreen()
        shuffleDeck()


def chooseCard():
    clearScreen()
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "Queen", "King", "Ace"]

    randomSuits = random.choice(suits)
    randomRanks = random.choice(ranks)

    print("Choosing a card.")
    time.sleep(0.5)
    clearScreen()
    print("Choosing a card..")
    time.sleep(0.5)
    clearScreen()
    print("Choosing a card...")
    time.sleep(1)
    clearScreen()

    print("Card Picker\n")
    print("Your card is: " + randomRanks + " of " + randomSuits)


def allCards():
    clearScreen()
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    suits.sort()
    ranks.sort(reverse=True)

    print("Displaying Deck.")
    time.sleep(0.5)
    clearScreen()
    print("Displaying Deck..")
    time.sleep(0.5)
    clearScreen()
    print("Displaying Deck...")
    time.sleep(1)
    clearScreen()

    for i in ranks:
        for j in suits:
            print(i + " of " + j)


def shuffleDeck():
    clearScreen()
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    deck = [j + " of " + i for j in ranks for i in suits]

    random.shuffle(deck)

    print("Shuffling Deck.")
    time.sleep(0.5)
    clearScreen()
    print("Shuffling Deck..")
    time.sleep(0.5)
    clearScreen()
    print("Shuffling Deck...")
    time.sleep(1)
    clearScreen()

    for i in deck:
        print(i)


clearScreen()
main()
