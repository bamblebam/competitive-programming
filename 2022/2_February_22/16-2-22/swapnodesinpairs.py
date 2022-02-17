# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=2
        dummy=ListNode()
        dummy.next=head
        curr,pre,nxt=dummy,dummy,dummy
        count=0
        
        while curr.next:
            count+=1
            curr=curr.next
            
        while count>=k:
            curr=new=pre.next
            nxt=curr.next
            for i in range(k-1):
                tmp=nxt.next
                nxt.next=curr
                curr=nxt
                nxt=tmp
            pre.next=curr
            new.next=nxt
            pre=new
            count-=k
        
        return dummy.next
            