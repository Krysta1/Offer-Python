class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        n = len(array)
        left, right = 0, n - 1

        while left < right:
            while left < n and array[left] % 2 != 0:
                left += 1
            while right > 0 and array[right] % 2 == 0:
                right -= 1
            if left < right:
                array[left], array[right] = array[right], array[left]
