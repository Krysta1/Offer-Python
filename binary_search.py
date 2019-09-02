def binary_search(test, num):
    start, end = 0, len(test) - 1
    while end >= start:
        middle = int((start + end) / 2)  # 这里也可以使用((end - start) >> 1) + start

        if test[middle] == num:
            return middle

        if test[middle] > num:
            end = middle - 1
        else:
            start = middle + 1

    return -1


def binary_search2(test, start, end, num):
    if end >= start:
        middle = int(start + (end - start) / 2)

        if test[middle] > num:
            return binary_search2(test, start, middle - 1, num)
        elif test[middle] < num:
            return binary_search2(test, middle + 1, end, num)
        else:
            return middle


def binary_search3(test, start, end, num):
    if end >= start:
        middle = int(start + (end - start) / 2)

        if test[middle] > num:
            end = middle - 1
        elif test[middle] < num:
            start = middle + 1
        else:
            return middle
    return binary_search2(test, start, end, num)


print(binary_search2([1, 2, 3, 4, 5, 6, 7], 0, 6, 7))
