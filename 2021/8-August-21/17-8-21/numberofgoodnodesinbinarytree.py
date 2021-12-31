# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,max_):
            nonlocal count
            if node is None:
                return False
            if max_<=node.val:
                count+=1
            max_=max(max_,node.val)
            dfs(node.left,max_)
            dfs(node.right,max_)
        dfs(root,root.val)
        return count