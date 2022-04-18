# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        use recursion
        go to the rightest node then keep on updating the value of the nodes
        """
        curr=0
        def helper(node):
            nonlocal curr
            if node is None:
                return 0
            
            helper(node.right)
            curr+=node.val
            node.val=curr
            helper(node.left)

            
        helper(root)
        return root