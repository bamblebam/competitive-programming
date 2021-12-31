
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def length(node):
            count = 0
            current = node
            if current is None:
                return 0
            while current is not None:
                count += 1
                current = current.next
            return count

        def solve(node):
            n = length(node)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(node.val)
            previous = None
            middle = node
            for _ in range(n//2):
                previous = middle
                middle = middle.next
            if previous is not None:
                previous.next = None
            nxt = middle.next
            middle.next = None
            root = TreeNode(middle.val)
            root.left = solve(node)
            root.right = solve(nxt)
            return root
        return solve(head)
