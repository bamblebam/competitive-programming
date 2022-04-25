class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n=len(scores)
        top3=defaultdict(list)
        
        def getTop3(a,b,e):
            bisect.insort_left(top3[a],[e,b])
            if len(top3[a])>3:
                top3[a].pop(0)
        
        for a,b in edges:
            getTop3(a,b, scores[b])
            getTop3(b,a,scores[a])
        
        ans=-1
        for a,b in edges:
            if len(top3[a])<2 or len(top3[b])<2:
                continue
            for c in top3[a]:
                for d in top3[b]:
                    #check if the nodes aren't the same
                    if c[1] not in [a,b] and d[1] not in [a,b] and c[1]!=d[1]:
                        ans=max(ans,scores[a]+scores[b]+c[0]+d[0])
        
        return ans
            