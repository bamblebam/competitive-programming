class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        nodesB = set()
        while headB is not None:
            nodesB.add(headB)
            headB = headB.next
        while headA is not None:
            if headA in nodesB:
                return headA
            headA = headA.next
        return None
