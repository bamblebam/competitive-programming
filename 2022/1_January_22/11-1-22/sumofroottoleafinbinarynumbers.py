# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans=0
        def helper(node,num):
            nonlocal ans
            if node is None:
                return 
            num+=str(node.val)
            if not node.left and not node.right:
                ans+=int(num,2)
                print(ans)
            helper(node.left,num)
            helper(node.right,num)
        
        helper(root,"")
        return ans
                