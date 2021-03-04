class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursivebt(self, pre, start, end, preorder, inorder):
        if pre > len(preorder)-1 or start > end:
            return None
        node = TreeNode(preorder[pre])
        inindex = inorder.index(preorder[pre])
        node.left = self.recursivebt(
            pre+1, start, inindex-1, preorder, inorder)
        node.right = self.recursivebt(
            pre+inindex-start+1, inindex+1, end, preorder, inorder)
        return node

    def buildTree(self, preorder, inorder):
        return self.recursivebt(0, 0, len(preorder)-1, preorder, inorder)
