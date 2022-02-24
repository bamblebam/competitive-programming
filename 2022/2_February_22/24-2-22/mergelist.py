# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use merge sort algorithm
        divide the list in 2 parts using slow,fast pointer method
        then get the left and right part of the list using the sortlist func
        then merge it
        '''
        def getMid(head):
            slow,fast=head,head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            mid=slow.next
            slow.next=None
            return mid
        
        def merge(head1,head2):
            dummy=tail=ListNode(0)
            while head1 and head2:
                if head1.val<head2.val:
                    tail.next,tail,head1=head1,head1,head1.next
                else:
                    tail.next,tail,head2=head2,head2,head2.next
            tail.next=head1 or head2
            return dummy.next
        
        if not head or not head.next:
            return head
        mid=getMid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return merge(left,right)