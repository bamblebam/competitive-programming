class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        '''
        greedy approach
        start adding even numbers starting from 2 and decrement the finalSUm by that
        if the sum is less than even num just add the remaining to the last num
        '''
        if finalSum%2:
            return list()
        curr=2
        ans=list()
        while finalSum>=curr:
            ans.append(curr)
            finalSum-=curr
            curr+=2
        ans[-1]+=finalSum
        return ans