def power(base, exponent):
    if base == 0.0 and exponent < 0:
        return -1

    return power_core(base, exponent)


def power2(base, exponent):
    if base == 0.0 and exponent < 0:
        return -1
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    res = power_core(base, exponent >> 1)
    res *= res
    if exponent & 1 == 1:
        res *= base

    return res


def power_core(base, exponent):
    unsigned_exponent = abs(exponent)
    res = 1
    for _ in range(unsigned_exponent):
        res *= base
    if exponent < 0:
        res = 1 / res
    return res


print(power2(-3, 3 ))
