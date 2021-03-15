class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = list()
        answers = list()
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr[k-1], arr[len(arr)-k] = arr[len(arr)-k], arr[k-1]
        for val in arr:
            answers.append(ListNode(val))
        for i in range(len(answers)):
            if i != len(answers)-1:
                answers[i].next = answers[i+1]
        return answers[0]
