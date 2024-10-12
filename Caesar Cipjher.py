def encrypt(text,length):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + length-65) % 26 + 65)

        else:
            result += chr((ord(char) + length - 97) % 26 + 97)

    return result


if __name__ == '__main__':
    while True:
        text = input("Enter text to cipher: ")
        shift = int(input("Enter a number to shift: "))
        toCiper = encrypt(text, shift)

        print(f"Ciphered text: {toCiper}")

        if text or shift or toCiper == "quit":
            exit()

