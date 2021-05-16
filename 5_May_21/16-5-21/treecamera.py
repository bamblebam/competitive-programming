
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        covered = {None}

        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if parent is None and node not in covered or node.left not in covered or node.right not in covered:
                    self.ans += 1
                    covered.update({parent, node, node.left, node.right})
        dfs(root)
        return self.ans
