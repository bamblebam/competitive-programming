# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=1
        dummy=head
        sentinel=ListNode(-1)
        sentinel.next=head
        if not head:
            return head
        while dummy.next:
            count+=1
            dummy=dummy.next
        k%=count
        if count==k or k==0:
            return head
        mid=head
        for i in range(count-k-1):
            mid=mid.next
        ans=mid.next
        dummy.next=head
        mid.next=None
        return ans
        