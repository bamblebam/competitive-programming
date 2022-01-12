# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #use dfs
        #go through the node if it is less than val go right else left
        #if node at that particular point doesn't exist then that is where the new node needs to be added
        def dfs(node):
            if node.val>val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left=TreeNode(val)
            else:
                if node.val<val:
                    if node.right:
                        dfs(node.right)
                    else:
                        node.right=TreeNode(val)
        
        if not root:
            return TreeNode(val)
        dfs(root)
        return root
        