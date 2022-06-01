class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr=deque(sorted(capacity[i]-rocks[i] for i in range(len(capacity))))
        ans=0
        while arr:
            x=arr.popleft()
            if x>additionalRocks:
                break
            ans+=1
            additionalRocks-=x
        return ans