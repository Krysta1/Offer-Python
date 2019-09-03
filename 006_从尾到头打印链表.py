class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversing_print(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next

    while stack:
        print(stack.pop())


def reversing_print_recursion(links):
    if links:
        print(links.val)
        reversing_print_recursion(links.next)

