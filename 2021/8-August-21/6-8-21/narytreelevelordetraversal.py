"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node'):
        if root is None:
            return list()
        
        def nodeToVal(arr):
            temp=list()
            for node in arr:
                temp.append(node.val)
            return temp
        
        queue=[root]
        ans=list()
        ans.append(nodeToVal(queue))
        queue.append(None)
        
        while queue:
            node=queue.pop(0)
            if node is None and queue:
                ans.append(nodeToVal(queue))
                queue.append(None)
                continue
            if node is not None:
                queue.extend(node.children)
 
        return ans