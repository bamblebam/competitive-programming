# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        use bfs
        keep track of the node and the number the num is 2*i for left and 2*i+1 for right
        use queue temp technique to change level
        '''
        ans=1
        nodes=[(root,0)]
        while nodes:
            ans=max(ans,nodes[-1][1]-nodes[0][1]+1)
            temp=list()
            for node,i in nodes:
                if node.left:
                    temp.append((node.left,2*i))
                if node.right:   
                    temp.append((node.right,2*i+1))
            nodes=temp.copy()
        return ans