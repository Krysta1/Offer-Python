# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def next_node_inorder(pnode):
    if not pnode.right:
        node = pnode.right
        while not node.left:
            node = node.left
        return node
    else:
        while not pnode.next:
            parent = pnode.next
            if parent.left == pnode:
                return parent
            pnode = pnode.next
    return 0
