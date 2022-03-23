# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        create a dict and store the value of each horizontal lvl in it
        use dfs to update horizontal and vertical lvl
        """
        dic=defaultdict(list)
        min_l=float('inf')
        max_l=-float('inf')
        def dfs(node,h,v):
            nonlocal min_l
            nonlocal max_l
            min_l=min(min_l,h)
            max_l=max(max_l,h)
            dic[h].append((v,node.val))
            if node.left:
                dfs(node.left,h-1,v+1)
            if node.right:
                dfs(node.right,h+1,v+1)
        dfs(root,0,0)
        output=list()
        for v in range(min_l,max_l+1):
            x=[j for i,j in sorted(dic[v])]
            output.append(x)
        return output