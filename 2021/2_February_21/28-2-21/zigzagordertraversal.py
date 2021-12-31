class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return list()
        currentlevel, nextlevel = list(), list()
        answers = dict()
        level = 1
        dir = False
        currentlevel.append(root)
        while len(currentlevel) > 0:
            if level not in answers:
                templist = list()
                for node in currentlevel:
                    templist.append(node.val)
                answers[level] = templist
            temp = currentlevel.pop()
            if dir:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            else:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)
            if len(currentlevel) == 0:
                nextlevel, currentlevel = currentlevel, nextlevel
                level += 1
                dir = not dir
        return answers.values()
