def has_path(matrix, rows, cols, path):
    if len(matrix) == 0 or rows <= 0 or cols <= 0 or len(path) == 0:
        return False

    visited = [0] * (rows * cols)
    path_length = 0
    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, path, path_length, visited):
                return True
    return False


def has_path_core(matrix, rows, cols, row, col, path, path_length, visited):
    if len(path) == path_length:
        return True

    flag = False
    if 0 <= row < rows and 0 <= col < cols and matrix[row*cols+col] == path[path_length] and not visited[row*cols+col]:
        path_length += 1
        visited[row*cols+col] = 1
        flag = has_path_core(matrix, rows, cols, row, col - 1, path, path_length, visited) or \
            has_path_core(matrix, rows, cols, row - 1, col, path, path_length, visited) or \
            has_path_core(matrix, rows, cols, row + 1, col, path, path_length, visited) or \
            has_path_core(matrix, rows, cols, row, col + 1, path, path_length, visited)
        if not flag:
            path_length -= 1
            visited[row*cols+col] = 0
    return flag


print(has_path('abtgcfcsjdeh', 3, 4, 'bfce'))
print(has_path('abtgcfcsjdeh', 3, 4, 'abcz'))

