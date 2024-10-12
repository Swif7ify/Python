def GCD(n1,n2):
    maximum = max(n1, n2)
    emp_lst = []

    for mx in range(1, maximum):
        r1 = n1 % mx
        r2 = n2 % mx
        if r1 == 0 and r2 == 0:
            emp_lst.append(mx)

    MAX = max(emp_lst)
    print(MAX)

GCD(42, 30)