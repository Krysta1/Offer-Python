# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            node = self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            node = self.stack2.pop()
        return node
        # return xx
