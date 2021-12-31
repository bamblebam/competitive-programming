# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node=head
        def createTree(node):
            if node is None:
                return
            if node.next is None:
                return TreeNode(node.val)
            mid=None
            curr=node
            temp=node
            prev=node
            i=0
            while temp is not None and temp.next is not None:
                temp=temp.next.next
                curr=curr.next
                if i>0:
                    prev=prev.next
                i+=1
            prev.next=None
            currNode=TreeNode(curr.val)
            left=createTree(node)
            right=createTree(curr.next)
            currNode.left=left
            currNode.right=right
            return currNode
        return createTree(head)