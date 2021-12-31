# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        node=root
        def helper(node):
            if not node:
                return False
            left=helper(node.left)
            right=helper(node.right)
            if not left:
                node.left=None
            if not right:
                node.right=None
            return node.val or left or right
        return root if helper(root) else None
            
            
        