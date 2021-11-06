# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #use dfs to go through all the root to leaf paths and add the sum to the ans
        ans=0
        def dfs(node,num):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right: #if child node add to ans
                ans+=num
            if node.left: #dfs on left subtree
                dfs(node.left,num*10+node.left.val)
            if node.right:
                dfs(node.right,num*10+node.right.val) #dfs on right subtree
        dfs(root,root.val)
        return ans