# row = 5
# column = 5
# symbol = "* "
#
# for i in range(row):
#     for j in range(column):
#         print(symbol, end=" ")
#     print()

# row = 5
# column = 5
# symbol = "* "
#
# for i in range(row):
#     for j in range(column):
#         if i == 0 or i == row - 1 or j == 0 or j == column - 1:
#             print(symbol, end=" ")
#         else:
#             print("  ", end=" ")
#     print()

# def pyramid(height):
#     for i in range(height):
#         # Print leading spaces
#         for j in range(height - i - 1):
#             print("  ", end=" ")
#         # Print stars
#         for k in range(2 * i + 1):
#             print("* ", end=" ")
#         # Move to the next line
#         print()
#
# pyramid_height = 5
# pyramid(pyramid_height)


# fibonacci
#
# n1 = 0
# n2 = 1
# next = n2
#
# for i in range(20):
#     n1, n2 = n2, next
#     next = n1 + n2
#     print(next)
#
# name = "Earl"
# age = 19
# weight = 69.23
# height = 169.5
#
# print(f"Your name is " + name)
# print(f"You age is {age}")
# print(f"Your weight is {weight}")
# print(f"Your height is {height}")


# def test():
#     name = input("Enter name")
#     return name
#
# def prints():
#     name = test()
#     return name
#
# print(prints())
#
# tie = "absABS ABS"
# tie = (tie).title()
#
# print(tie)
#
# import os
#
# pathf = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\test\\read.txt"
# pathd = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\test"
# pathc = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\writing.txt"
#
# if os.path.exists(pathf):
#     print(pathf)
#     print("This exist in the device")
#     if os.path.isdir(pathf):
#         print("this is not a directory")
#     elif os.path.isfile(pathf):
#         print("this is a file")
# print()
# if os.path.exists(pathd):
#     print(pathd)
#     print("This exist in the device")
#     if os.path.isdir(pathd):
#         print("this is a file directory")
#     elif os.path.isfile(pathd):
#         print("this is a file")
# print()
# text = "This is a overwrite!"
#
# with open(pathf) as file:
#     print(file.read())
# print()
# with open(pathc) as file:
#     print(file.read())
#
# with open(pathc, "w") as file:
#     file.write(text)
#
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# def combine():
#     user = input("Enter a number separated by spaces: ")
#     userInputs = user.split()
#
#     try:
#         userInputs = [int(i) for i in userInputs]
#     except ValueError:
#         return combine()
#
#     return userInputs
#
# numbers = combine()
# result = add(*numbers)
# print(result)

# import os

# path = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\test\\bot\\bot.txt"
# text = "abcdefghijklmnopqrstuvwxyz"
#
# with open(path) as file:
#     print(file.read())

# text = "ZYXWVUTSRQPONMLKJIHGFEDCBA".lower()
#
# print(text)

# # Initialize an empty list
# numbers = []
#
# # Populate the list with numbers from 1 to 10
# for num in range(1, 11):
#     numbers.append(num)
#
# # Print the populated list
# print("List of numbers:", numbers)

# # Initialize an empty list
# fruits = []
#
# # List of fruit names to add
# fruit_names = ["apple", "banana", "cherry", "date", "elderberry"]
#
# # Populate the list with fruit names
# for fruit in fruit_names:
#     fruits.append(fruit)
#
# # Print the populated list
# print("List of fruits:", fruits)
#
# import random
#
# rows = 3
# cols = 3
#
# a_line = ["A", "B", "C", "D"]
# b_line = ["A", "B", "C", "D"]
# c_line = ["A", "B", "C", "D"]
#
# slot = [a_line, b_line, c_line]
#
# for i in range(rows):
#     print(random.choice(a_line), end=" ")
# print(" ")
#
# for i in range(rows):
#     print(random.choice(b_line), end=" ")
# print(" ")
#
# for i in range(rows):
#     print(random.choice(c_line), end=" ")
# print(" ")
#
# if slot[0][0] and slot and slot[1][0] and slot[2][0]:
#     print("YES")
# elif slot == [0][1] and slot[1][1] and slot[2][1]:
#     print("YES")
# elif slot == [0][2] and slot[1][2] and slot[2][2]:
#     print("YES")
# else:
#     print("NO")

# import random
#
# rows = 3
# cols = 3
#
# a_line = ["A", "B", "C", "D"]
# b_line = ["A", "B", "C", "D"]
# c_line = ["A", "B", "C", "D"]
#
# slot = [a_line, b_line, c_line]
#
# # Randomly selecting items for each row
# selected_rows = [
#     [random.choice(a_line) for _ in range(cols)],
#     [random.choice(b_line) for _ in range(cols)],
#     [random.choice(c_line) for _ in range(cols)]
# ]
#
# # Printing the selected items
# for row in selected_rows:
#     print(" ".join(row))
#
# print(" ")

# # Check for a winning condition in columns
# win = False
# for col in range(cols):
#     if selected_rows[0][col] == selected_rows[1][col] == selected_rows[2][col]:
#         win = True
#         break

# win = False
# for row in selected_rows:
#     if row[0] == row[1] == row[2]:
#         win = True
#         break
#
# if win:
#     print("YES")
# else:
#     print("NO")

# hol = {"A": 5, "B": 6, "C": 7, "D": 8, "E": 9, "F": 10}
#
# value = hol.get("A")
#
# print(value)

# hol = {"A": 5, "B": 6, "C": 7, "D": 8, "E": 9, "F": 10}
#
# # Fetch values for both "A" and "B"
# values = [hol.get("A"), hol.get("B")]
#
# print(values)  # Output: [5, 6]


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 == 1:
#         print("Weird")
#     elif n % 1 == 0:
#         if 2 <= n <= 5:
#             print("Not Weird")
#         elif n > 20:
#             print("Not Weird")
#         elif 6 <= n <= 20:
#             print("Weird")


# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#
#     sum = a + b
#     diff = a - b
#     pro = a * b
#
#     print(sum, diff, pro)

# if __name__ == '__main__':
#     n = int(input())
#
#     for i in range(n):
#         if i < n:
#             power = i ** 2
#             print(power)

# year = 1920
#
#
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0:
#     print("not leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("not leap year")
# if year % 400 == 0 or year % 4 == 0 and year % 100 !=0:
# def myfunc(n):
#     return lambda a: a * n
#
#
# doubler = myfunc(2)
# triplet = myfunc(3)
#
# print(doubler(11))
# print(triplet(11))


# numbers = [[i for k in range(10)] for i in range(1,11)]
#
# print(numbers)


# num = list(map(int, input().split())).sort() # or sorted arr1 = sorted(num)
#
# print(num)

# permutation
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# n = int(input("Enter n: "))
#
# permutation = [[i, j, k] for i in range(num1 + 1) for j in range(num2 + 1) for k in range(num3 + 1) if i + j + k != n]
# print(permutation)

# adding values to a empty sey
# empty = set()
# fruits = {"banana", "Apple", "orange"}
#
# for fruit in fruits:
#     empty.add(fruit)
#
#     print(empty)


# adding values to empty list
# empty = []
# animals = ["dog", "cat", "giraffe", "crow"]
#
# for animal in animals:
#     empty.append(animal)
#
#     print(empty)

# adding values to empty dict
# empty = {}
# animals = {"dog": 1, "cat": 2, "fish": 3}
#
# for key, value in animals.items():
#     empty[key] = value
#
# print(empty)
#
# empty = {}
# animals = {"dog": 1, "cat": 2, "fish": 3}
#
# empty.update(animals)
#
# print(empty)


# usagwe of len
# fruits = {"apple", "banana", "cherry"}
# name = "Earl Romeo B Ordovez"

# num_of_fruits = len(fruits)
# len_of_name = len(name)
# print(len(name))
# print(len_of_name)
#
# print(num_of_fruits)

# question_num = 0
#
# th = {"20-1": "A", "20+10": "B", "30+10": "C", "40+60": "D"}
#
# td = [
#     ["A. 20"], ["B. 30"], ["C. 40"], ["D 100"]
# ]
# for j in th:
#     for i in td[question_num]:
#         print(i)
#         question_num += 1

# n = int(input())
# arr = map(int, input().split())
# the runner up scroe
#
# lst = ["2", "2", "1", "3", "6", "5", "4"]
#
# arr = list(set(lst))
# arr.sort()
# runner_up = arr[-2]
# high_score = arr[-1]
# print(runner_up)
# print(high_score)


# # lambda func, sorting 2d list with numbers
# py_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# sorted_students = sorted(py_students, key=lambda student: student[1])
# highest = max(py_students)
# print(py_students)
# #
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#
#         py_studs = []
#         py_studs.append([name, score])
#
#         sorted_studs = sorted(py_studs, key=lambda student: student[1])
#
#         lowest = sorted_studs[0][0]
#         scn_low = sorted_studs[1][0]
#
#         print(lowest)
#         print(scn_low)


# sorting grads and determining the secone lowest grade
#
# if __name__ == '__main__':
#     py_studs = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         py_studs.append([name, score])
#
#     # Get all the unique grades in sorted order
#     sorted_grades = sorted(set([student[1] for student in py_studs]))
#
#     # The second lowest grade
#     second_lowest_grade = sorted_grades[1]
#
#     # Get the names of students with the second lowest grade
#     second_lowest_students = [student[0] for student in py_studs if student[1] == second_lowest_grade]
#
#     # Sort the names alphabetically
#     second_lowest_students.sort()
#
#     # Print each name on a new line
#     for student in second_lowest_students:
#         print(student)


# name, *line = input("B").split() # takes one input and place it into the name and the rest is in the *line
#
# print(name)
# print(*line) # printing with * joins the list


# map allows you do have a fucntion in a interable object
#
# animal = ["cow", "dog", "cat", "horse", "zebra", "elephant"]
# length = list(map(len, animal))
# num = 0
# for lengths in length:
#     print(lengths, end=" ")
#     print(animal[num])
#     num += 1
# print(length)
# animal = ["cow", "dog", "cat", "horse", "zebra", "elephant"]
# length = list(map(lambda x: len(x), animal))
# print(length)
# animal = ["cow", "dog", "cat", "horse", "zebra", "elephant"]
#
#
# def add_s(string):
#     return string + "s"
#
#
# add_letter = list(map(add_s, animal))
#
# print(add_letter)


# filter if the function returns true it will keep it otherwise it wil not
# def longer_than_4(string):
#     return len(string) > 4
#
#
# animal = ["cow", "dog", "cat", "horse", "zebra", "elephant"]
# filtered = list(filter(longer_than_4, animal))
# lam = list(filter(lambda x: len(x) > 4, animal))
# print(filtered)
# print(lam)


# zip combining list
# animal = ["cow", "dog", "cat", "horse", "zebra", "elephant"]
# ages = ["19", "220", "10", "16"]

# for idx in range(min(len(animal), len(ages))):
#     animals = animal[idx]
#     age = ages[idx]
#     print(f"{animals} is {age} years old")
#
# combined = list(zip(animal, ages))
#
# for name, age in combined:
#     print(f"{name}: {age}")
#
# for index, (name, age) in enumerate(combined, 1):
#     print(f"{index}: {name}: {age}")


# calculating the average inside a liist
#
# lst = [96, 95, 95, 92, 94, 99]
#
# total_sum = sum(lst)
# print(total_sum)
# num_of_elem = len(lst)
# print(num_of_elem)
#
# average = total_sum / num_of_elem
#
# print(f"{average:.2f}")
#
# if __name__ == '__main__':
#     n = int(input())  # Number of students
#     student_marks = {}
# 
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#
#     query_name = input()  # Name of the student to query
#
#     # Get the scores for the queried student
#     query_scores = student_marks[query_name]
#
#     # Calculate the average
#     sum_of_num = sum(query_scores)
#     len_of_num = len(query_scores)
#     average = sum_of_num / len_of_num
#
#     # Print the average formatted to 2 decimal places
#     print("{:.2f}".format(average))


# diamond
# height = 5
# for i in range(height):
#     for j in range(height - i - 1):
#         print("  ", end=" ")
#     for k in range(2 * i + 1):
#         print("* ", end=" ")
#     print(" ")
#
# for l in range(height):
#     for m in range(l + 1):
#         print("  ", end=" ")
#     for n in range(2 * (height - m) - 3):
#         print("* ", end=" ")
#     print(" ")

# height = 5
# # rhombus
# for l in range(height):
#     for m in range(l):
#         print(" ", end=" ")
#     for n in range(2 * (height - 1) - 1):
#         print("* ", end=" ")
#     print(" ")

# square but alternating
# row = 10
# col = 10
# for i in range(row):
#     for j in range(col):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 print(" ", end=" ")
#             else:
#                 print("*", end=" ")
#         else:
#             if j % 2 == 0:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#
#     print()

# # left side pyramid
# row = 5
# col = 5
#
# for i in range(row):
#     for j in range(col - i):
#         print("*", end=" ")
#
#     print()

# half pyramid leftside
# row = 5
# col = 5
#
# for i in range(row):
#     for j in range(1 + i):
#         print("*", end=" ")
#
#     print()


# # full pyramidmn on the left side
# row = 5
# col = 5
# for i in range(row):
#     for j in range(1 + i):
#         print("*", end=" ")
#     print()
#
# for k in range(col):
#     for l in range(col - k - 1):
#         print("*", end=" ")
#     print()
#
# import getpass
#
# username = input("Enter your username: ")
# password = getpass.getpass("Enter your password: ")
#
# print(f"Hello {username}!")
# print(f"Hello {getpass.getuser()}!")


# pyramid upside down no inside
#
# row = 5
# col = 9
#
# for i in range(row):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for k in range(col - i - j):
#         if (i == 0 or k == 0 or i == row - 1
#                 or k == col - (2 * i) - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#   * * * * * * * * *
#     *           *
#       *       *
#         *   *
#           *


# import tracemalloc
#
# tracemalloc.start()
#
# # Your code here
# lst = []
# print("Enter the food you like")
# print("Duplicates are not allowed\n")
#
# while True:
#     food = input("Enter your favorite food: ")
#     if food == "quit":
#         break
#     if food in lst:
#         print("You already have that food")
#     else:
#         lst.append(food)
#
# print(*lst)
#
# # Display the memory usage
# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')
#
# print("[ Top 10 memory-consuming lines ]")
# for stat in top_stats[:10]:
#     print(stat)

# def mutate(string):
#     lst = list(string)
#     print(lst)
#     return lst
#
#
# s = input("String")  # split every character
# s = input("String").split()  # split per spaces
# new_s = mutate(s)
# print(new_s)
# string mutation
# def mutate_string(string, position, character):
#     lst = list(string)
#     lst[position] = character
#     string = "".join(lst)
#     return string
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# finding substring in string
# def count_substring(string, sub_string):
#     total = 0
#     for i in range(len(string)): # ABCDCDC - CDC
#         if string[i:len(string)].startswith(sub_string):
#             total += 1
#     return total
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
#
# string = "ABCDCDC"
# sub_string = "CDC"
# count = 0
#
# # Loop through the string, stopping early enough so that sub_string can fit
# for i in range(len(string) - len(sub_string) + 1): # 5
#     # Check if the substring matches the part of the string
#     if string[i:i+len(sub_string)] == sub_string:
#         count += 1
#
# print(count)


# validators
# if __name__ == '__main__': # cannot use any outside loops,
#     s = input("qA2")
#     print(any(i.isalnum() for i in s))
#     print(any(i.isalpha() for i in s))
#     print(any(i.isdigit() for i in s))
#     print(any(i.islower() for i in s))
#     print(any(i.isupper() for i in s))


# textwrap
# import textwrap
# # ABCDEFGHIJKLIMNOQRSTUVWXYZ
#
# def wrap(string, max_width): # this put it into list and separate based on width (wrap)
#     maxi = textwrap.wrap(string, max_width)
#     return maxi
#
# def fill(string, max_width): # this make it similar to for loop printing
#     maxi = textwrap.fill(string, max_width)
#     return maxi
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input()) # 5
#     result = fill(string, max_width)
#     print(result)


# n, m = map(int,input().split())
# for i in range(n//2):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))
# print('WELCOME'.center(m,'-'))
# for i in reversed(range(n//2)):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))

# text = "Hello World"
# print(text.center(1080, "-"))


# logic for guessing the word
# guess = input("Guess a letter: ").upper()

# gets the guess, loops in the entire list of the word and if there a match it finds that index[idx] and place that with
# your guess

# if guess in secret_word:
#     for idx, char in enumerate(secret_word):
#         if guess == char:
#             fill_in[idx] = guess

# else:
#     random = random.choice(secret_word)
#     for idx, char in enumerate(secret_word):
#         if random == char:
#             fill_in[idx] = random


# def recursive(n): # having the same function under its function
#     if n == 1:
#         return 1
#     return n * recursive(n-1)
#
# print(recursive(5))
# fac = int(input("Enter a number: "))
# result = 1
#
# for i in range(1, fac + 1):
#     result *= i
#
# print(result)


# guess = input("Guess a number: ").upper()
# lst = ["L", "I", "S", "T"]
#
#
# for char in guess:
#     print(char)
#     if char in lst:
#         print(True)
#     else:
#         print(False)

# hangman_picture = [
#     " -----",
#     " |   |",
#     " O   |",
#     "/|\\  |",  # Note: Use "\\" to escape the backslash for the arm.
#     "/ \\  |",
#     "     |"
# ]
#
# # Calculate the margin (number of spaces) for centering
# margin = 10  # Adjust this number based on your console width
#
# for line in hangman_picture:
#     print(" " * margin + line)

# def print_hangman(stage):
#     margin = 5  # Adjust this number based on your console width
#
#     # Define each stage of the hangman
#     stages = [
#         [" ----"],  # Rope
#         [" ----", "  O"],  # Head
#         [" ----", "  O", "  |"],  # Body
#         [" ----", "  O", " /|"],  # Left Arm
#         [" ----", "  O", " /|\\"],  # Right Arm
#         [" ----", "  O", " /|\\", " /"],  # Left Leg
#         [" ----", "  O", " /|\\", " / \\"],  # Right Leg
#     ]
#
#     # Print the current stage with centering
#     for line in stages[stage]:
#         print(" " * margin + line)
#
#
# # Example usage: Print hangman at different stages
# for i in range(7):
#     print_hangman(i)
#     print("\n" * 2)  # Separate stages with some space

# def print_hangman(stage):
#     margin = 10  # Adjust this number based on your console width
#
#     # Define each stage of the hangman with the stand included
#     stages = [
#         [
#             " -----",
#             " |    ",
#             " |   ",
#             " |   ",
#             " |   ",
#             " |   ",
#             " |   "
#         ],  #
#         [
#             " -----",
#             " |   |",
#             " |   ",
#             " |   ",
#             " |   ",
#             " |   ",
#             " |   "
#         ],  # Stand and Rope
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |   ",
#             " |   ",
#             " |   ",
#             " |   "
#         ],  # Head
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |   |",
#             " |   |",
#             " |   ",
#             " |   "
#         ],  # Body
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |  /|",
#             " |   |",
#             " |   ",
#             " |   "
#         ],  # Left Arm
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |  /|\\",
#             " |   |",
#             " |   ",
#             " |   "
#         ],  # R
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |  /|\\",
#             " |   |",
#             " |  /",
#             " |   "
#         ],  # Left Leg
#         [
#             " -----",
#             " |   |",
#             " |   O",
#             " |  /|\\",
#             " |   |",
#             " |  / \\",
#             " |   "
#         ],  #  # Right Leg
#     ]
#
#     for line in stages[stage]:
#         print(" " * margin + line)
#
#
# for i in range(8):
#     print_hangman(i)
#     print("\n" * 2)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# n = int(input("Enter a number: "))
#
# permutation = [[i,j,k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1)]
#
# print(permutation)



# def recursive_denominator(d):
#         if d == 1:
#                 return 1
#         return d * recursive_denominator(d - 1)
#
# def recursive_nominator(n):
#         if n == 1:
#                 return 1
#         return n * recursive_nominator(n - 1)
#
# denominator = recursive_denominator(16)
# nominator = recursive_nominator(13)
#
# result = denominator / nominator
#
# print(result)

# path = "C:\\Users\\earlo\\OneDrive\\Desktop\\python\\writing.txt"
# text = "The quick brown fox jumps over the lazy dog"
# with open(path, "w") as file:
#     file.write(text)
#
# import pyautogui
# import time
#
# time.sleep(2)
# pyautogui.typewrite(text)


# text = "calculator_but_it_is_not_a_normal_calculator_it_is_a_calculator_that_can_literally_solve_human_crisis"
#
# for char in text:
#     for letter in char:
#         print(letter)

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n - 1)
#
# def sum_of_fact(a, b):
#     return factorial(a) + factorial(b)
#
# pro = sum_of_fact(5, 5)
# print(pro)
#
# import math
#
# def custom_floor(x):
#     return int(x) if x >= 0 else int(x) - 1

# def custom_floor(x):
#     if x >= 0:
#         return int(x)
#     else:
#         result = int(x) - 1
#
#     return result

# def custom_ceil(x):
#     return int(x) if x == int(x) else int(x) + 1
#
# num1 = custom_floor(1)
# num2 = custom_floor(0)
#
# num3 = custom_ceil(1)
# num4 = custom_ceil(0)
#
# num6 = math.ceil(5.4)
#
# print(num1, num2, num3, num4, num6)


