class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        pre = 0
        idx_map = {value: index for index, value in enumerate(inorder)}

        def helper(left, right):
            nonlocal pre
            if left > right:
                return None
            root_val = preorder[pre]
            root = TreeNode(root_val)
            pre += 1
            root.left = helper(left, idx_map[root_val]-1)
            root.right = helper(idx_map[root_val]+1, right)
            return root
        return helper(0, len(preorder)-1)
