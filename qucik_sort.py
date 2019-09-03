def quick_sort(data):
    if len(data) <= 1:
        return data

    else:
        pivot = data.pop()
        smaller = []
        larger = []

        for num in data:
            if num < pivot:
                smaller.append(num)
            else:
                larger.append(num)

        return quick_sort(smaller) + [pivot] + quick_sort(larger)


def quick_sort2(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quick_sort2(data, left, pivot - 1)
        quick_sort2(data, pivot, right)
    return data


def partition(data, left, right):
    pivot = data[int((left + right) / 2)]

    while left <= right:
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1

        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    return left


print(quick_sort2([6, 2, 3, 2, 4, 5, 7, 7], 0, 7))
print(quick_sort([6, 2, 3, 2, 4, 5, 7, 7]))
