def quinaryAdd(n1, n2):
    decimal_sum = int(n1, 5) + int(n2, 5)
    return to_quinary(decimal_sum)

def to_quinary(decimal_num):
    if decimal_num == 0:
        return '0'

    quinary_num = ''
    while decimal_num > 0:
        quinary_num = str(decimal_num % 5) + quinary_num
        decimal_num //= 5
    return quinary_num

result = quinaryAdd('13', '24')
print(result)