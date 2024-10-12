def binaryAdd(n1, n2):
    return bin(int(n1, 2) + int(n2, 2))[2:]

result = binaryAdd('1101', '100')
print(result)