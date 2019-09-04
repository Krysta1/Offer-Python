def max_product_cutting(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length < 3:
        return 2
    products = [0] * (length + 1)
    products[0:4] = [0, 1, 2, 3]
    for i in range(4, length + 1):
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i-j]
            if products[i] < product:
                products[i] = product
            print(products)
    res = products[length]
    return res


def max_product_greed(length):  # 大于5尽量剪3的小段，贪婪解法。
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length < 3:
        return 2

    time_three = length // 3
    length = length - 3 * time_three
    if length == 0:
        res = 3 ** time_three
    elif length == 1:
        res = 2 * 2 * 3 ** (time_three - 1)
    else:
        res = 2 * 3 * 3 ** (time_three - 1)

    return res


print(max_product_cutting(100))
print(max_product_greed(100))
