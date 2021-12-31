# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        ans = list()
        # count nodes
        node = head
        while node is not None:
            count += 1
            node = node.next
        # if k is greater or equal than the number of nodes
        if k >= count:
            for i in range(k):
                temp = list()
                if head:
                    x = head
                    head = head.next
                    x.next = None
                    temp.append(x)
                if len(temp) == 0:
                    temp.append(ListNode(val=''))
                ans.extend(temp)
        # if k is smaller than the number of nodes
        else:
            parts = count//k
            extra = count % k
            for i in range(k):
                x = parts+1 if extra else parts
                extra = max(extra-1, 0)
                prev = head
                for i in range(x-1):
                    head = head.next
                new_head = head.next
                head.next = None
                ans.append(prev)
                head = new_head

        return ans
