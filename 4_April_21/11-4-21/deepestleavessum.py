
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root):
        if root is None:
            return list()
        queue = list()
        temp = list()
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif queue:
                queue.append(None)
                temp = list()
        return sum(temp)
