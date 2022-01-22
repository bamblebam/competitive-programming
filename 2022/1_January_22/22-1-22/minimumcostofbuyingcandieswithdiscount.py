class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        count=0
        i=1
        while cost:
            x=cost.pop(0)
            if i%3==0:
                i+=1
                continue
            count+=x
            i+=1
        return count