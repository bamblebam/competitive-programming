# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        mod=10**9+7
        def dfs(node):
            if node is None:
                return 0
            ans=node.val+dfs(node.left)+dfs(node.right)
            sum_list.append(ans)
            return ans
        sum_list=list()
        dfs(root)
        total=max(sum_list)
        return max(i*(total-i) for i in sum_list)%mod