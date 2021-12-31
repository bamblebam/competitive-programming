# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        #use recursion to get the tilt of the leftest and rightest nodes
        #then return the sum of its left right and node val as sum till the upper node
        ans=0
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            ans+=abs(left-right)
            return left+right+node.val
        helper(root)
        return ans