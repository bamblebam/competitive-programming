# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #use dfs to find all the root to leaf words and then reverse them and choose the    minimum
        ans="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        def dfs(node,word):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right: #if leaf check with the ans
                ans=min(ans,word[::-1])
            if node.left:
                dfs(node.left,word+chr(97+node.left.val)) #dfs on left subtree
            if node.right:
                dfs(node.right,word+chr(97+node.right.val)) #dfs on right subtree
        dfs(root,chr(root.val+97))
        return ans