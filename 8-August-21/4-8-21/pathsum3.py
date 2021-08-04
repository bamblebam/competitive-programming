# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.ans=0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def helper(node,curr_sum):
            if node is None:
                return
            curr_sum+=node.val
            if curr_sum==targetSum:
                self.ans+=1
            if node.left:
                helper(node.left,curr_sum)
            if node.right:
                helper(node.right,curr_sum)
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            helper(node,0)
            inorder(node.right)
        
        inorder(root)
        return self.ans