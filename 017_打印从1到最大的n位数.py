def print_1_to_max(n):
    if n <= 0:
        return -1
    digits = [0] * n
    print_digits_recursivly(digits, len(digits), 0)


def print_digits_recursivly(digits, length, index):
    if index == length:
        print_digits(digits)
        return

    for i in range(0, 10):
        digits[index] = str(i)
        print_digits_recursivly(digits, length, index + 1)


def print_digits(digits):
    is_begin_with_zero = True
    result = ''
    for num in digits:
        if is_begin_with_zero and num != '0':
            is_begin_with_zero = False
        if not is_begin_with_zero:
            result += num
    if result != '':
        print(result)


print(print_1_to_max(100))
