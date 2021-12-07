class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # count nunmber of chips in odd position and number of chips in even position. The ans is the minimum of the two.
#         This is because you move all the even chips to 0 and odd ones to 1 for 0 cost
#then you only have to move them from 0 to 1 or 1 to 0
        n=len(position)
        odd=0
        for i in position:
            if i%2:
                odd+=1
        return min(odd,n-odd)