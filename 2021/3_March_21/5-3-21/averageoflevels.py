import statistics


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if root is None:
            return list()
        answers = list()
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
                answers.append(statistics.mean(temp))
                temp = list()
        answers.append(statistics.mean(temp))
        return answers
