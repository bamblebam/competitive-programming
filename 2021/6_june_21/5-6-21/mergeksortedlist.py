import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        h = []
        for i in lists:
            head = i
            while head:
                heapq.heappush(h, head.val)
                head = head.next
        a = ListNode(0)
        ans = a
        while h:
            temp = heapq.heappop(h)
            ans.next = ListNode(temp)
            ans = ans.next
        return a.next
