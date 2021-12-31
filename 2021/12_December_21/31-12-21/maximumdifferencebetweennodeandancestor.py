# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #bottom up dp
        #find the min and max of each subtree and compare it with the curr val
        #if diff is greater update ans
        #can also be done in top down manner
        ans=float("-inf")
        def helper(node):
            nonlocal ans
            if not node:
                return 0,0
            val=node.val
            min_,max_=val,val
            lmx,lmn,rmx,rmn=val,val,val,val
            if node.left:
                lmx,lmn=helper(node.left)
            if node.right:
                rmx,rmn=helper(node.right)
            max_=max(lmx,rmx,max_)
            min_=min(rmn,lmn,min_)
            ans=max(ans,abs(max_-val),abs(min_-val))
            return max_,min_
        helper(root)
        return ans
            