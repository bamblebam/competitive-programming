# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        idx=bisect.bisect(preorder,preorder[0])
        root.left=self.bstFromPreorder(preorder[1:idx])
        root.right=self.bstFromPreorder(preorder[idx:])
        return root