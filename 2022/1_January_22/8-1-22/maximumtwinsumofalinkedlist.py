# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=deque()
        while head:
            arr.append(head.val)
            head=head.next
        ans=0
        while arr:
            x1=arr.popleft()
            x2=arr.pop()
            ans=max(ans,x1+x2)
        return ans