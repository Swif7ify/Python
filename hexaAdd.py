def hexaAdd(n1, n2):
    return hex(int(n1, 16) + int(n2, 16))[2:]

result = hexaAdd('b', 'c')
print(result)