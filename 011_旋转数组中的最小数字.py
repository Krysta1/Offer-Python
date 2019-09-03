def minNumberInRotateArray(rotateArray):
    # write code here
    n = len(rotateArray)
    if n == 0:
        return 0

    left, right = 0, n - 1
    while left < right:
    # while rotateArray[left] >= rotateArray[right]:
    #     if left == right - 1:
    #         return rotateArray[right]
        middle = (left + right) // 2
        if rotateArray[middle - 1] > rotateArray[middle]:
            return rotateArray[middle]
        if rotateArray[middle + 1] < rotateArray[middle]:
            return rotateArray[middle + 1]

        if rotateArray[left] == rotateArray[right] == rotateArray[middle]:
            # 如果left right middle相等的话，会出错，所以加上判断进行顺序查找。
            return minNum(rotateArray, left, right)
        if rotateArray[middle] >= rotateArray[left]:
            left = middle
        else:
            right = middle

    return rotateArray[right]


def minNum(rotate, left, right):
    save_min = 99999
    for num in rotate[left: right]:
        if num < save_min:
            save_min = num

    return save_min


print(minNumberInRotateArray([3, 4, 5, 1, 2]))
print(minNumberInRotateArray([1, 1, 1, 0, 1]))  # 如果left right middle相等的话，会出错
print(minNumberInRotateArray([3]))
