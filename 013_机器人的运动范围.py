def has_path(k, rows, cols):
    if k < 0 or rows <= 0 or cols <= 0:
        return False

    visited = [0] * (rows * cols)
    return has_path_core(k, rows, cols, 0, 0, visited)


def has_path_core(k, rows, cols, row, col, visited):
    count = 0
    if 0 <= row < rows and 0 <= col < cols and if_valid(k, row, col) and not visited[row*cols+col]:
        # path_length += 1
        visited[row*cols+col] = 1
        count = 1 + has_path_core(k, rows, cols, row, col-1, visited) + \
            has_path_core(k, rows, cols, row-1, col, visited) + \
            has_path_core(k, rows, cols, row, col+1, visited) + \
            has_path_core(k, rows, cols, row+1, col, visited)
    return count


def if_valid(k, m, n):
    return sum([int(x) for x in str(m)]) + sum([int(x) for x in str(n)]) <= k


print(has_path(5, 10, 10))
print(has_path(18, 20, 20))

# print(if_valid(18, 35, 38))
