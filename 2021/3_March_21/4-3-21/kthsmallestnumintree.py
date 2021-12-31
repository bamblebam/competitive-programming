class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answers = list()

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.answers.append(root.val)
            self.inorder(root.right)

    def kthSmallest(self, root, k):
        self.answers = list()
        self.inorder(root)
        return self.answers[k-1]
