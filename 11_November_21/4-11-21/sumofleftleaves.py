# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #use dfs to traverse the tree and add the sum of left leaves to the ans
        #use isleft variable to know that if a node is left child of parent or not
        #if it is left child check if it is a leaf
        ans=0
        def dfs(node,isleft):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right and isleft:
                ans+=node.val
            if node.left:
                dfs(node.left,True)
            if node.right:
                dfs(node.right,False)
        dfs(root,False)
        return ans