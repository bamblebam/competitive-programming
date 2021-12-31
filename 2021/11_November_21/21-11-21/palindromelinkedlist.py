# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev=None
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next #reverses the first half of list rev points to the start of the reversed first half
        if fast:
            slow=slow.next #if len of list is odd makes sure that slow points to the second half
        while rev and rev.val==slow.val: #compare if the 2 halfs are palindromes
            slow=slow.next
            rev=rev.next
        return not rev