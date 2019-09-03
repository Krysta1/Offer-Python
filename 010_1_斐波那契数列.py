# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fibonacci_list = []
        if n > 39:
            return -1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        first = 1
        second = 1
        fibonacci_list.append(first)
        fibonacci_list.append(second)

        for i in range(n - 2):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

        return fibonacci_list[-1]

    def fibonacci_recursion(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursion(n-1) + self.fibonacci_recursion(n-2)

