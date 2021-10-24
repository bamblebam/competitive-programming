# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) solution
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     n=0
    #     def inorder(node):
    #         nonlocal n
    #         if node is None:
    #             return
    #         inorder(node.left)
    #         n+=1
    #         inorder(node.right)
    #     inorder(root)
    #     return n
    
    # O(log(n)^2) solution
    def path(self,root,num):
        # check if the number exists, convert the num to binary and take all except 1st bit.
        # if 0 go left else right will find the num in a complete binary tree
        for i in bin(num)[3:]:
            if i=='0':
                root=root.left
            else:
                root=root.right
            if not root:
                return False
        return True
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # find the depth of the binary tree. Then set the left and right bound for final layer.
        # use binary search to see if the node exists
        if not root:
            return 0
        temp,depth=root,0
        while temp.left:
            temp,depth=temp.left,depth+1
        l,r=1<<depth,(1<<(depth+1))-1
        if self.path(root,r):
            return r
        while l+1<r:
            mid=(l+r)//2
            if self.path(root,mid):
                l=mid
            else:
                r=mid
        return l