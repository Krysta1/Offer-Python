def duplicate(test):  # 时间复杂度On 空间复杂度O1的

    count = 0
    if len(test) == 0:  # if list length is 0 return 0
        return count

    for num in test:  # if element in test <0 or >(n-1)
        if num < 0 or num > (len(test) - 1):
            return 0

    for i in range(len(test)):  #
        m = test[i]
        if m == i:  # i == test[i] 没有问题
            continue
        else:
            if m == test[m]:  # test[i] == test[test[i]]说明一个比这个位置小的数字出现在不该在的位置，前面已经出现过这个数字。
                count += 1
            else:  # 不相等就把test[i]放到该放的位置上。
                tmp = test[i]
                test[i] = test[m]
                test[m] = tmp

    return count


def duplicate2(test):
    count = 0
    if len(test) == 0:  # if list length is 0 return 0
        return count

    for num in test:  # if element in test <0 or >(n-1)
        if num < 0 or num > (len(test) - 1):
            return 0

    tmp = [-1] * len(test)
    for num in test:
        if tmp[num] == -1:
            tmp[num] = num
        else:
            if tmp[num] == -2:
                continue
            tmp[num] = -2
            count += 1

    return count


def duplicate3(test):
    count = 0
    if len(test) == 0:  # if list length is 0 return 0
        return count

    for num in test:  # if element in test <0 or >(n-1)
        if num < 0 or num > (len(test) - 1):
            return 0

    for i in range(len(test)):
        for j in range(0, len(test) - i - 1):
            if test[j] > test[j + 1]:
                test[j], test[j + 1] = test[j + 1], test[j]

    print(test)

    i, j = 0, 1
    while j < len(test):
        if test[i] != test[j]:
            i = j
            j += 1
            continue
        elif j == i + 1:
            count += 1
            j += 1
        else:
            j += 1

    return count


# test cases
print(duplicate3([2, 3, 1, 0, 2, 5, 3]))

print(duplicate3([2, 3, 1, 0, 2, 5, 4]))

print(duplicate3([]))

print(duplicate3([2, 3, 1, 0, 2, 5, 9]))

print(duplicate3([2, 3, 1, 1, 2, 1, 3, 0]))
