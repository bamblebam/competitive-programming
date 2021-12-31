class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        queue = list()
        queue.append((root, -1))
        temp = list()
        while queue:
            node, node_parent = queue.pop()
            if node.left:
                temp.append((node.left, node))
            if node.right:
                temp.append((node.right, node))
            if not queue:
                x_par, y_par = False, False
                for value, parent in temp:
                    if value.val == x:
                        x_par = parent
                    if value.val == y:
                        y_par = parent
                    if x_par and y_par and x_par != y_par:
                        return True
                queue, temp = temp, queue
        return False

    
        # alternative solution
        # def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # #put all elements in queue according to their level, use None to separate them, check lvl of required stuff
        # queue=deque([(root,None),(None,None)])
        # l=0
        # a,b=0,0
        # while queue:
        #     node,par=queue.popleft()
        #     if node is None and queue:
        #         queue.append((None,None))
        #         l+=1
        #         continue
        #     if node is None:
        #         break
        #     if node.val==x:
        #         a=(par,l)
        #     if node.val==y:
        #         b=(par,l)
        #     if node.left:
        #         queue.append((node.left,node))
        #     if node.right:
        #         queue.append((node.right,node))
        # return a[1]==b[1] and a[0]!=b[0]
            