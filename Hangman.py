import os
import time
import random

import hangman_draw as hangman

secret_word = []
fill_in = []
guesses = []
CHANCES = 7


def main():
    guess = input("Guess a letter: ").upper().replace(" ", "")
    return guess

def randomizer():
    lst = [
        "GALAXY", "UNIVERSE", "COMET", "ASTEROID", "PLANET", "MOON", "STARDUST", "ECLIPSE",
        "COSMOS", "BLACKHOLE", "SUPERNOVAS", "NEBULA", "ORBIT", "METEOR", "SUN", "SOLAR",
        "CONSTELLATION", "SPACE", "ASTRO", "LIGHTYEAR", "QUASAR", "WORMHOLE", "ZENITH", "HORIZON",
        "VORTEX", "EQUINOX", "AURORA", "GLOBE", "CONTINENT", "OCEAN", "ISLAND", "DESERT",
        "MOUNTAIN", "FOREST", "RIVER", "LAKE", "VALLEY", "CANYON", "CAVE", "FJORD",
        "PLAIN", "JUNGLE", "TUNDRA", "VOLCANO", "GEYSER", "CORAL", "REEF", "GROTTO",
        "HAVEN", "SANCTUARY", "MEADOW", "OASIS", "WILDERNESS", "HIGHLAND", "FOOTHILL", "CLIFF"
    ]
    randomize = random.choice(lst)

    for char in randomize:
        secret_word.append(char)

    for _ in secret_word:
        fill_in.append("_")

    return secret_word, fill_in, randomize


def draw(tries):
    if tries == 7:
        print()
    else:
        hangman.print_hangman(tries)

def check_answer(guess, secret_word, fill_in, tries, win):
    clear_screen()
    if guess in guesses:
        print("You have already guessed that letter!")
    elif guess == "HINT":
        while True:
            cheat = random.choice(secret_word)
            if cheat in fill_in:
                continue
            else:
                break
        guess = cheat
        pass
    else:
        guesses.append(guess)

    for letter in guess:
        if letter in secret_word:
            for idx, char in enumerate(secret_word):
                if letter == char:
                    fill_in[idx] = letter
        else:
            tries -= 1
            print(f"Sorry, you guessed the wrong letter ({letter}).")
            if tries == 0:
                print("You lose.")
                try_again()

    if "_" not in fill_in or guess == win:
        print(f"You won! The word was {win}")
        try_again()

    return tries


def try_again():
    while True:
        choice = input("Would you like to play again? (y/n): ").lower()
        if choice.islower():
            if choice == "y":
                clear_screen()
                secret_word[:] = []
                fill_in[:] = []
                guesses[:] = []
                play_game(CHANCES)
            else:
                print("Thanks for playing!")
                time.sleep(1)
                exit()
        else:
            print("Thanks for playing!")
            time.sleep(1)
            exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game(chance):
    secret_word, fill_in, win = randomizer()
    print("WELCOME TO HANGMAN!")
    while True:
        print(" ".join(fill_in))
        print("Your Guesses:", *guesses)
        print(f"Remaining tries: {chance}")
        guess = main()
        tries = check_answer(guess, secret_word, fill_in, chance, win)
        chance = tries
        draw(chance)

if __name__ == "__main__":
    play_game(CHANCES)

