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


print(max_product_cutting(10))
