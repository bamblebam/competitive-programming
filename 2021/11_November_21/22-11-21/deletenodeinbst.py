# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #there are 4 scenarios that can happen
        #node has no child,only left or only right child, just remove then node and replace in this case
        #in case where node has both children go to node.right and then left till end, replace node value with left value and remove that node.
        if not root:
            return None
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.right and root.left:
                temp=root.right
                while temp.left:
                    temp=temp.left
                root.val=temp.val
                root.right=self.deleteNode(root.right,root.val)
        elif root.val>key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root