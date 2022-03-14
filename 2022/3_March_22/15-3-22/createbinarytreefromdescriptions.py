# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        use dict to keep track of the parent and child nodes
        """
        node_map=dict()
        is_child=set()
        for parent,child,is_left in descriptions:
            if parent in node_map:
                node=node_map[parent]
            else:
                node=TreeNode(parent)
                node_map[parent]=node
                node=node_map[parent]
            if child in node_map:
                x=node_map[child]
            else:
                x=TreeNode(child)
                node_map[child]=x
                x=node_map[child]
            if is_left:
                node.left=x
            else:
                node.right=x
            is_child.add(child)
        for k in node_map.keys():
            if k not in is_child:
                return node_map[k]
                