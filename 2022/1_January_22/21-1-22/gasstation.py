class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #kadanes algorithm
        #add the array to itself to take into account the circular aspect
        #go through the array adding the gas and subtracting the cost
        #if the curr is -ve that means not enough gas start from next idx
        n=len(cost)
        gas=gas+gas
        cost=cost+cost
        start=0
        curr=0
        for i,(g,c) in enumerate(zip(gas,cost)):
            nxt=curr+g-c
            if nxt<0:
                curr=0
                start=i+1
            else:
                curr=nxt
            if i-start>=n:
                return start
        return -1