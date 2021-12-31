# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #just like with preorder but...
        #get the last element instead of the first and solve the right tree first
        idx_map={value:idx for idx,value in enumerate(inorder)}
        post=len(postorder)-1
        def helper(left,right):
            nonlocal post
            if left>right:
                return None
            root_val=postorder[post]
            root=TreeNode(root_val)
            post-=1
            root.right=helper(idx_map[root_val]+1,right)
            root.left=helper(left,idx_map[root_val]-1)
            return root
        return helper(0,len(postorder)-1)