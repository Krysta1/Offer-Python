def search_in_matrix(test, num):  # from top right
    if len(test) == 0:
        return -1

    i, j = 0, len(test[0]) - 1
    while i < len(test) and j >= 0:
        if test[i][j] == num:
            return i, j
        elif test[i][j] > num:
            j -= 1
        else:
            i += 1
    return -1


def search_in_matrix2(test, num):  # from below left
    if len(test) == 0:
        return -1

    i, j = len(test) - 1, 0
    while i >= 0 and j < len(test[0]):
        if test[i][j] == num:
            return i, j
        elif test[i][j] < num:
            j += 1
        else:
            i -= 1
    return -1


print(search_in_matrix2([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 7))
