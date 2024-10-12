from math import factorial

def pascalTriangle(row):
    for i in range(row):
        for j in range(row-i+1):
            print(end="  ")

        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end="   ")

        print()

pascalTriangle(6)