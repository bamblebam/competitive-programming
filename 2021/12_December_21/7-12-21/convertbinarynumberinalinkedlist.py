# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node=head
        count=-1
        ans=0
        while node:
            node=node.next
            count+=1
        while head:
            ans+=head.val*(2**count)
            count-=1
            head=head.next
        return ans