class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        p = pListHead
        while p:
            count += 1
            p = p.next

        if k > count:
            return None

        for _ in range(count - k):
            pListHead = pListHead.next

        return pListHead
