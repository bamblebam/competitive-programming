class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            curr = p == node or q == node
            if curr+left+right >= 2:
                self.ans = node
            return curr or left or right
        helper(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def __init__(self):
#         self.ans=None
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         p,q=p.val,q.val
#         def helper(node):
#             if node is None:
#                 return False
#             left=helper(node.left)
#             right=helper(node.right)
#             curr=p==node.val or q==node.val
#             if curr+left+right>=2:
#                 self.ans=node
#             return curr or left or right
#         helper(root)
#         return self.ans
