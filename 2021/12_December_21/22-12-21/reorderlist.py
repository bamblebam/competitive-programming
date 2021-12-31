# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #split the list in 2 parts at the middle, reverse the second part, merge these 2 lists alternatively
        #thats the pattern
        
        #if no head return
        if not head:
            return list()
        
        #find middle
        slow,fast=head,head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        
        #reverse second list
        prev,curr=None,slow.next
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        slow.next=None #separating the 2 lists
        
        #merge the 2 lists alternatively
        head1,head2=head,prev
        while head2:
            nxt=head1.next
            head1.next=head2
            head1=head2
            head2=nxt