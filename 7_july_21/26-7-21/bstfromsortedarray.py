# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        n=len(nums)
        def createTree(arr):
            if len(arr)==1:
                return TreeNode(arr[0])
            mid=len(arr)//2
            print(arr[mid])
            node=TreeNode(arr[mid])
            left=createTree(arr[:mid])
            right=None
            if mid+1<len(arr):
                right=createTree(arr[mid+1:])
            node.left=left
            node.right=right
            return node
        return createTree(nums)