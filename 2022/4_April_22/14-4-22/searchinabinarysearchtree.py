# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=0
        def helper(node):
            nonlocal ans
            if not node:
                return
            x=node.val
            if x==val:
                ans=node
                return
            elif x>val:
                helper(node.left)
            else:
                helper(node.right)
        helper(root)
        if not ans or not root:
            return None
        return ans