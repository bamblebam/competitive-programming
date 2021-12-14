# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            
            if low<=node.val<=high:
                ans+=node.val
                helper(node.left)
                helper(node.right)
                
            if node.val>high:
                helper(node.left)
            
            if node.val<low:
                helper(node.right)
        helper(root)
        return ans
            