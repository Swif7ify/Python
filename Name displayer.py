# def combine():
#     user = input("Enter a name separated by spaces: ")
#     userInputs = user.split()
#
#     return userInputs
#
#
# numbers = combine()
# result = numbers
#
# for i, j in enumerate(result, 1):
#     print(f"{i}. {j}")

#
# names = set()
#
# while True:
#     # Get user input
#     user_name = input("Please enter a username (leave blank to display usernames): ")
#
#     # If the user provides a name, add it to the set
#     if user_name:
#         names.add(user_name)
#     else:
#         # If the input is blank, break the loop
#         break
#
#
# for i, j in enumerate(names, 1):
#     print(f"{i}. {j}")


names = []

while True:
    user_name = input("Enter your name (leave blank to exit): ")
    if user_name:
        names.append(user_name)
    else:
        break


for i, j in enumerate(names, 1):
    print(f"{i}. {j}")

