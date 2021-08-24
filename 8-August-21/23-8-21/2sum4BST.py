# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, target: int) -> bool:
        nums = set()
        flag = False

        def inorder(node):
            nonlocal flag
            if not node:
                return
            inorder(node.left)
            if target-node.val in nums:
                flag = True
                return True
            nums.add(node.val)
            inorder(node.right)

        inorder(root)
        return flag
