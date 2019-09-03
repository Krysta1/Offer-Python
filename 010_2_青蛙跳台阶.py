# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = [0, 1, 2]
        if number == 1 or number == 2:
            return a[number]

        for i in range(number - 2):
            a.append(a[-1] + a[-2])
        return a[-1]
