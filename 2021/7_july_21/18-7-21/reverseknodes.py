# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        temp = head
        new_head = None
        while temp is not None:
            temp = temp.next
            n += 1
        cycles = n//k
        curr = head
        prev = None
        for i in range(cycles):
            temp_list = list()
            for j in range(k):
                temp_list.append(curr)
                curr = curr.next
            last = curr
            for m in range(k):
                if m == 0:
                    temp_list[m].next = last
                else:
                    temp_list[m].next = temp_list[m-1]
            if i == 0:
                new_head = temp_list[-1]
            else:
                prev.next = temp_list[-1]
            prev = temp_list[0]
            curr = last
        return new_head
