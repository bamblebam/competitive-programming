class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        current = list()
        next = list()
        current.append(root)
        if d == 1:
            return TreeNode(v, root)
        for _ in range(2, d):
            for _ in range(len(current)):
                node = current.pop(0)
                if node:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
            next, current = current, next
        for node in current:
            left = TreeNode(v)
            right = TreeNode(v)
            left.left = node.left
            right.right = node.right
            node.left = left
            node.right = right
        return root
