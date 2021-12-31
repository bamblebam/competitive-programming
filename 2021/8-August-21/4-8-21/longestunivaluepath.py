# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans=0
        def helper(node):
            if node is None:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            left_count=right_count=0
            if node.left and node.left.val==node.val:
                left_count=left+1
            if node.right and node.right.val==node.val:
                right_count=right+1
            self.ans=max(self.ans,left_count+right_count)
            return max(right_count,left_count)
        helper(root)
        return self.ans