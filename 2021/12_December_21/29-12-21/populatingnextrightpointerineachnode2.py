"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue=deque([root])
        temp=deque()
        while queue:
            node=queue.popleft()
            if not queue:
                node.next=None
            else:
                node.next=queue[0]
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not queue:
                queue=temp
                temp=deque()
        return root