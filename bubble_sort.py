def bubble_sort(test):
    if not test or len(test) == 0:
        return 0

    for i in range(len(test)):
        for j in range(0, len(test) - i - 1):
            if test[j] > test[j + 1]:
                test[j], test[j + 1] = test[j + 1], test[j]

    return test


print(bubble_sort([2, 1, 4, 3]))
