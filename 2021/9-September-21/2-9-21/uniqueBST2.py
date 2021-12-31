# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(first, last):
            return [TreeNode(val, left, right) for val in range(first, last+1) for left in helper(first, val-1) for right in helper(val+1, last)] or [None]
        return helper(1, n)
