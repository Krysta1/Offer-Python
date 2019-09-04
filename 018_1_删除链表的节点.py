class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead, node):
        # write code here
        if node == pHead:
            del node

        if node.next is None:
            while pHead:
                if pHead.next == node:
                    pHead.next = None
                pHead = pHead.next
        else:
            node.val == node.next.val
            n_node = node.next
            node.next = n_node.next
            del n_node
