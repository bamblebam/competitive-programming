# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(root):
            if root is None:
                return (0,0)
            left=max(dfs(root.left))
            right=max(dfs(root.right))
            self.ans=max(self.ans,left+right)
            return (left+1,right+1)
        dfs(root)
        return self.ans
            
            