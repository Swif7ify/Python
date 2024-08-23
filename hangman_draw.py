def print_hangman(stage):
    margin = 10  # Adjust this number based on your console width

    # Define each stage of the hangman with the stand included
    stages = [
        [
            " -----",
            " |   |",
            " |   O",
            " |  /|\\",
            " |   |",
            " |  / \\",
            " |   "
        ],  # Right Leg
        [
            " -----",
            " |   |",
            " |   O",
            " |  /|\\",
            " |   |",
            " |  /",
            " |   "
        ],  # Left Leg
        [
            " -----",
            " |   |",
            " |   O",
            " |  /|\\",
            " |   |",
            " |   ",
            " |   "
        ],  # Right Arm
        [
            " -----",
            " |   |",
            " |   O",
            " |  /|",
            " |   |",
            " |   ",
            " |   "
        ],  # Left Arm
        [
            " -----",
            " |   |",
            " |   O",
            " |   |",
            " |   |",
            " |   ",
            " |   "
        ],  # Body
        [
            " -----",
            " |   |",
            " |   O",
            " |   ",
            " |   ",
            " |   ",
            " |   "
        ],  # Head
        [
            " -----",
            " |   |",
            " |   ",
            " |   ",
            " |   ",
            " |   ",
            " |   "
        ]  # Stand and Rope
    ]

    # Print the hangman stage with the specified margin
    for line in stages[stage]:
        print(" " * margin + line)