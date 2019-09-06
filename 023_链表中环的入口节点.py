class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = head, head

        while first and second:
            first = first.next
            second = second.next
            if second:
                second = second.next
            else:
                return 0

            if first == second:
                first = head
                while first != second:
                    first = first.next
                    second = second.next
                break
        return second
