# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        prev=None
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow,prev=slow.next,slow
        if fast.next:
            slow,prev=slow.next,slow
        if not prev:
            return None
        prev.next=slow.next
        return head