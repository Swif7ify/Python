# import random
#
# def random_number():
#     randomizer = random.randint(1, 50)
#     return randomizer
#
# if __name__ == '__main__':
#     secret_number = random_number()
#     guesses = []
#
#     while True:
#         guess = int(input("Guess a number between 1 and 50: "))
#         if guess == secret_number:
#             print(f"You won")
#             print(f"Number of guesses: {len(guesses)}")
#             break
#         else:
#             if guess in guesses:
#                 print("You already guessed this number")
#                 continue
#             else:
#                 guesses.append(guess)
#
#             if guess > secret_number:
#                 print("Your guess is too large")
#             elif guess < secret_number:
#                 print("Your guess is too small")


# leap_year = 2024
# count = 0
#
# for year in range(leap_year, 3000):
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         count += 1
#         print(f'{count}: {year}')
#         if count == 5:
#             break


# import math
#
# lst = []
#
# for i in range(2, 100):
#     if len(lst) >= 10:
#         break
#     is_prime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         lst.append(i)
#
# print(*lst)


# def recursive_sum_of_N(n):
#     if n == 0:
#         return 0
#     return n + recursive_sum_of_N(n-1)
#
# user_input = int(input("Enter a number: "))
# print(recursive_sum_of_N(user_input))


# lst = []
#
# print("Enter the food you like")
# print("Duplicates are not allowed\n")
#
# while True:
#     food = input("Enter your favorite food: ")
#     if food == "quit":
#         break
#     elif food in lst:
#         print("You already have this")
#     else:
#         lst.append(food)
#
#
# print("\nYour favorite food is:")
# for i, j in enumerate(lst, 1):
#     print(f"{i}. {j}")
