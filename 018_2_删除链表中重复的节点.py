class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = ListNode(-1)
        dummy.next = pHead

        p = dummy
        while p.next:
            q = p.next
            while q and p.next.val == q.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return dummy.next


# 注意dummy的使用，在链表前添加一个节点，可以免去处理头节点的情况。
