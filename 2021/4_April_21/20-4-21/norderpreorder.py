
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        if root is None:
            return list()
        stack, answer = [root], list()
        while stack:
            cur = stack.pop()
            answer.append(cur.val)
            stack.extend(cur.children[::-1])
        return answer
