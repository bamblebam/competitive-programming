class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = list(), list()
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next
        num1 = int("".join(map(str, reversed(num1))))
        num2 = int("".join(map(str, reversed(num2))))
        num = list(map(int, reversed(list(str(num1+num2)))))
        answer = list()
        for i in range(len(num)):
            answer.append(ListNode(num[i]))
        for i in range(len(answer)):
            if i != len(answer)-1:
                answer[i].next = answer[i+1]
        return answer[0]
