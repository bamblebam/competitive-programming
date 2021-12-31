from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums):
        ans=list()
        sl=SortedList()
        for num in nums[::-1]:
            index=sl.bisect_left(num)
            ans.append(index)
            sl.add(num)
        return ans[::-1]