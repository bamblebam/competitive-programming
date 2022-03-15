class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        excavated_sites=set()
        for x,y in dig:
            excavated_sites.add((x,y))
        
        @lru_cache(None)
        def helper(r1,c1,r2,c2):
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    if (i,j) not in excavated_sites:
                        return 0
            return 1
                                                
        ans=0
        for r1,c1,r2,c2 in artifacts:
            ans+=helper(r1,c1,r2,c2)
        
        return ans