import os
import time
import subprocess


def clearScreen():
    try:
        if os.name == "nt":
            subprocess.run("cls", check=True, shell=True)
        else:
            subprocess.run("clear", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Failed to clear the screen.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def userInputs():
    clearScreen()

    print("Welcome to BMI Calculator\n")
    name = input("Enter your name: ").title()
    age = input("Enter your age: ")
    weight = input("Enter your weight(kg): ")
    height = input("Enter your height(cm): ")

    try:
        age = int(age)
        weight = int(weight)
        height = int(height)
    except ValueError:
        clearScreen()
        print("Please input correct values!")
        time.sleep(1.5)
        clearScreen()
        return userInputs()

    return name, age, weight, height


def calculation(weight, height):
    userHeight = float(height * 0.01)
    userBmi = weight / (userHeight * userHeight)
    return userBmi


def showInformation(name, age, weight, height, userBmi):
    clearScreen()
    if userBmi <= 18.5:
        classification = "Underweight"

    elif userBmi <= 24.9:
        classification = "Normal"

    elif userBmi <= 30:
        classification = "Overweight"

    else:
        classification = "Obese"

    print("Name: " + name)
    print(f"Age: {age}")
    print(f"Weight: {weight}(kg)")
    print(f"Height: {height}(cm)\n")
    print(f"Classification: ({userBmi:.2f}) {classification}")


clearScreen()
name, age, weight, height = userInputs()
userBmi = calculation(weight, height)
showInformation(name, age, weight, height, userBmi)
