class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return None
        prev = None
        curr = head
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        first = prev
        last = curr
        while right > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            right -= 1
        if first:
            first.next = prev
        else:
            head = prev
        last.next = curr
        return head
