def number_of_1(num):
    count = 0
    while num:
        count += 1
        num = (num-1) & num
    return count


def number_of_one(num):
    count = 0
    flag = 1
    for i in range(32):  # 这里因为python属性问题，可以一直增大大正无穷，128次循环。
        if num & flag:
            count += 1
        flag = flag << 1
        # num = num >> 1
        # print(flag)
    return count


print(number_of_1(0x7FFFFFFF))
print(number_of_one(10))
