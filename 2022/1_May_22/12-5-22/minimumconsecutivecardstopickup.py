class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indices=defaultdict(list)
        for i,c in enumerate(cards):
            indices[c].append(i)
        ans=float('inf')
        for k,v in indices.items():
            if len(v)>=2:
                for i in range(1,len(v)):
                    ans=min(ans,v[i]-v[i-1]+1)
                    
        return ans if ans!=float('inf') else -1