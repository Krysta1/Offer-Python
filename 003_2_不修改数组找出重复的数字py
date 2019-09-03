def get_duplicate(test):
    n = len(test)
    if n == 0 or not test:
        return 0

    start, end = 1, n - 1
    while end >= start:
        middle = int((start + end) / 2)  # 注意转化成int型
        # print(middle)

        count = 0
        for num in test:
            if start <= num <= middle:
                count += 1

        if end == start:
            if count > 1:
                return start
            else:
                break

        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1

    return -1


print(get_duplicate([2, 3, 5, 4, 3, 2, 6, 7]))
