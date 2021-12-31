# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node=root
        p=p.val
        q=q.val
        while True:
            val=node.val
            if p==val or q==val:
                return node
            if p>val and q>val:
                node=node.right
            elif p<val and q<val:
                node=node.left
            else:
                return node
        