import os

GUESSES = []
CORRECT_GUESSES = 0

questions = {"What does CPU stand for?": "B",
             "Which of the following is considered the brain of the computer?": "C",
             "Which of the following is a non-volatile memory?": "B",
             "What is the main function of an operating system?": "B",
             "Which component is responsible for rendering images, video, and animations?": "D",
             "What does RAM stand for?": "C",
             "Which device is primarily used for permanent data storage?": "C",
             "What type of software is designed to help users perform a specific task?": "B",
             "Which of the following is an example of an input device?": "C",
             "Which protocol is commonly used to transfer web pages on the internet?": "B"}

answers = [
    ["A. Central Process Unit", "B. Central Processing Unit", "C. Central Programming Unit",
     "D. Computer Personal Unit"],
    ["A. RAM", "B. Hard Drive", "C. CPU", "D. GPU"],
    ["A. RAM", "B. ROM ", "C. Cache", "D. Register"],
    ["A. To perform arithmetic operations", "B. To manage computer hardware and software resources ",
     "C. To edit documents", "D. To design graphics"],
    ["A. Sound Card", "B. Motherboard", "C. Network Card", "D. Graphics Card"],
    ["A. Real-time Access Memory", "B. Readily Available Memory", "C. Random Access Memory", "D. Read Access Memory"],
    ["A. CPU", "B. RAM", "C. Hard Drive", "D. GPU"],
    ["A. System Software", "B. Application Software", "C. Utility Software", "D. Malware"],
    ["A. Monitor", "B. Printer", "C. Keyboard ", "D. Speaker"],
    ["A. FTP", "B. HTTP", "C. SMTP", "D. IP"]
]


def new_game(guesses, correct_guess, questions, options):
    question_num = 0

    for question in questions:
        print("<-------------------------------------------------------------------->")
        print(question)

        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(question), guess)
        question_num += 1

    display_score(correct_guess, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


def display_score(correct_guess, guesses):
    print("<-------------------------------------------------------------------->")
    print("Results")
    print("<-------------------------------------------------------------------->")

    print("Answer: ", end="")
    for i, j in enumerate(questions, 1):
        print(f"{i}). {questions.get(j)}", end="  |")
    print()

    print("Guesses: ", end="")
    for i, j in enumerate(guesses, 1):
        print(f"{i}). {j}", end="  |")
    print()

    score = int((correct_guess / len(questions))*100)
    print(f"Score: {score}%", end="")


def play_again():
    response = input("\nWould you like to play again? (y/n): ").lower()
    if response == "y":
        return True
    else:
        return False


new_game(GUESSES, CORRECT_GUESSES, questions, answers)

while play_again():
    new_game(GUESSES, CORRECT_GUESSES, questions, answers)

print("Thanks for playing!")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")