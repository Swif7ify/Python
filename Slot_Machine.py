import os
import random

MAX_BET = 10000
MIN_BET = 100

MIN_LINES = 1
MAX_LINES = 3

MIN_BET_LINES = 5
MAX_BET_LINES = 5000

ROWS = 3
COLS = 3

WINNINGS = 0

a_line = ["🍋", "🍎", "🍎", "🍏", "🍏", "🍑", "🍑", "🍑", "🍑", "🍑", "🍑"]
b_line = ["🍋", "🍎", "🍎", "🍏", "🍏", "🍑", "🍑", "🍑", "🍑", "🍑", "🍑"]
c_line = ["🍋", "🍎", "🍎", "🍏", "🍏", "🍑", "🍑", "🍑", "🍑", "🍑", "🍑"]

# a_line = ["🍏", "🍏", "🍏", "🍏", "🍏", "🍏", "🍏", "🍏"]
# b_line = ["🍎", "🍎", "🍎", "🍎", "🍎", "🍎", "🍎", "🍎"]
# c_line = ["🍋", "🍋", "🍋", "🍋", "🍋", "🍋", "🍋", "🍋"]

symbol_multipliers = {
    "🍋": 5,
    "🍎": 3,
    "🍏": 2,
    "🍑": 1.5
}


def slot_spin(cols):
    selected_rows = [
        [(random.choice(a_line)) for _ in range(cols)],
        [(random.choice(b_line)) for _ in range(cols)],
        [(random.choice(c_line)) for _ in range(cols)]
    ]

    for row in selected_rows:
        print(" | ".join(row))

    return selected_rows


def check_winnings(selected_rows, multiplier, symbols_value, bet, balance, lines):
    condition = False
    for row in selected_rows:
        if row[0] == row[1] == row[2]:
            if lines == 1:
                multiplier += symbols_value.get(row[0])
                condition = True
                break
            elif lines == 2:
                multiplier += symbols_value.get(row[0])
                if row == 1:
                    break
            else:
                multiplier += symbols_value.get(row[0])

            condition = True

    if condition:
        amount = bet * multiplier
        balance += amount
        print(f"You win ₱{amount}. Balance: ₱{balance} ")

    else:
        balance -= bet
        print(f"You lose ₱{bet}, Balance: ₱{balance}")

    return balance


def get_amount():
    while True:
        amount = input("Please input a amount(₱): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                clear_screen()
                print(f"Sorry, the amount must be between ₱{MIN_BET} and ₱{MAX_BET}")
        else:
            clear_screen()
            print("Please enter a valid amount!")

    return amount


def number_of_lines():
    while True:
        lines = input("Please input a number of lines to bet (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                clear_screen()
                print("Please enter a valid number of lines")

    return lines


def bet_on_lines(balance, lines):
    while True:
        bet = input("Please input a amount to bet on each line ₱(5-5000): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET_LINES <= bet <= MAX_BET_LINES:
                total_bet = bet * lines
                if balance < total_bet:
                    clear_screen()
                    print(
                        f"You don't have enough money to bet. Your balance is ₱{balance} and your bet is ₱{total_bet}")
                else:
                    break
            else:
                clear_screen()
                print(f"Sorry, the amount must be between ₱{MIN_BET_LINES} and ₱{MAX_BET_LINES}")
        else:
            clear_screen()
            print("Please enter a valid amount!")

    return total_bet


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_again(balance, lines, bet):
    while True:
        try_again = input("Would you like to modify values? (y/n) \n enter to continue: ").lower()
        if try_again == 'y':
            user_input = input("Do you want to change your (balance) (bet) (lines) or (quit) \n "
                               "enter to continue: ").lower()
            if user_input == 'balance':
                balance = get_amount()
            elif user_input == 'lines':
                lines = number_of_lines()
            elif user_input == 'bet':
                bet = bet_on_lines(balance, lines)
            elif user_input == 'quit':
                exit()
            elif user_input == "":
                return balance, lines, bet
            else:
                clear_screen()
                print("Sorry, the input is not valid!")
            return balance, lines, bet
        elif try_again == 'n':
            quit()
        elif try_again == "":
            return balance, lines, bet
        else:
            clear_screen()
            print("Sorry, the input is not valid!")


def main():
    clear_screen()
    balance = get_amount()
    lines = number_of_lines()
    bet = bet_on_lines(balance, lines)

    while True:
        clear_screen()
        print(f"Your previous balance ₱{balance}. You bet a total of ₱{bet}, on {lines} lines")
        spin = slot_spin(ROWS)
        balance = check_winnings(spin, WINNINGS, symbol_multipliers, bet, balance, lines)
        balance, lines, bet = start_again(balance, lines, bet)
        if balance < bet:
            print(f"You don't have enough money to bet. Your balance is ₱{balance} and your bet is ₱{bet}")
            balance = get_amount()
            

main()
