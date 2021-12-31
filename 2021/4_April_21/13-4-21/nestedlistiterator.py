from collections import deque

# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList):
        self.queue = deque(nestedList)

    def fix(self):
        last = self.queue.popleft()
        for num in last.getList()[::-1]:
            self.queue.appendleft(num)

    def next(self) -> int:
        first = self.queue[0]
        if first.isInteger():
            self.queue.popleft()
            return first.getInteger()
        else:
            self.fix()
            return self.next()

    def hasNext(self) -> bool:
        while self.queue and not self.queue[0].isInteger():
            self.fix()
        return self.queue
