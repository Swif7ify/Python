def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


lst = [1, 2, 4, 4, 7, 8, 1, 40, 2, 4, 10, 11, 12, 20]
result = bubbleSort(lst)
print(*result)
