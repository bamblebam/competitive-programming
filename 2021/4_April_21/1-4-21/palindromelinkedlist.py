
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        answer = list()
        while head is not None:
            answer.append(head.val)
            head = head.next
        if answer == list(reversed(answer)):
            return True
        return False
