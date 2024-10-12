import random

length = int(input("Enter the length of the password: "))

char = [chr(i) for i in range(33,127)]
hexa = [hex(i)[2:] for i in range(16)]
bina = [bin(i)[2:] for i in range(2)]
passwords = []

emp = ''.join(char) + ''.join(hexa) + ''.join(bina)
password = random.choices(emp, k = length)
security = ''.join(random.sample(password, length))

print(security)