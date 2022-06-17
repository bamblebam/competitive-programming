# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Let solve(node) be some information about how many cameras it takes to cover the subtree at this node in various states. There are essentially 3 states:

[State 0] Strict subtree: All the nodes below this node are covered, but not this node.
[State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
[State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).
Once we frame the problem in this way, the answer falls out:

To cover a strict subtree, the children of this node must be in state 1.
To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
To cover the subtree when placing a camera here, the children can be in any state.

        """
        def dp(node):
            if not node:
                return 0,0,float('inf')
            
            left=dp(node.left)
            right=dp(node.right)
            
            dp0=left[1]+right[1]
            dp1=min(left[2]+min(right[1:]),right[2]+min(left[1:]))
            dp2=min(left)+min(right)+1
            
            return dp0,dp1,dp2
        
        return min(dp(root)[1:])