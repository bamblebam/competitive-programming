# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodes=list()
        def inorder(node):
            if node.left:
                inorder(node.left)
            nodes.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        nodes_set=set(nodes)
        for node in nodes:
            if k-node in nodes_set and k-node != node:
                return True
        return False
                