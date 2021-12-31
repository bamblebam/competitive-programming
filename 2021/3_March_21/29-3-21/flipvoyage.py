
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.answers = list()
        self.index = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.index]:
                    self.answers = [-1]
                    return
                self.index += 1
                if self.index < len(voyage) and node.left and node.left.val != voyage[self.index]:
                    self.answers.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        if -1 in self.answers:
            return [-1]
        return self.answers
