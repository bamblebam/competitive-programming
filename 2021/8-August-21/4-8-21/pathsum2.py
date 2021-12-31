# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        ans=list()
        def helper(node,curr_sum,path):
            if node is None:
                return
            path.append(node.val)
            curr_sum+=node.val
            if curr_sum==targetSum:
                t=path.copy()
                if len(t)>0 and not node.left and not node.right:
                    ans.append(t)
            if node.left:
                helper(node.left,curr_sum,path)
                path.pop()
            if node.right:
                helper(node.right,curr_sum,path)
                path.pop()
                
        helper(root,0,list())
        return ans