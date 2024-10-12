def perfectNumber(n):
    perfect_numbers = []

    for i in range(1, n+1):
        sum_of_divisors = 0
        for j in range(1, i):
            if i % j == 0:
                sum_of_divisors += j

        if sum_of_divisors == i:
            perfect_numbers.append(i)

    print(perfect_numbers)