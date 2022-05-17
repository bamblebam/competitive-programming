# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans=None
        def inorder(node):
            nonlocal ans
            if node.left:
                inorder(node.left)
            if node.val==target.val:
                ans=node
            if node.right:
                inorder(node.right)
        if not cloned:
            return
        inorder(cloned)
        return ans