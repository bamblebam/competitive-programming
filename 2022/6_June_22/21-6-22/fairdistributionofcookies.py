class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        use backtracking to go over all the possible distributions of cookies and find the minimum
        """
        ans=float('inf')
        fair=[0]*k
        n=len(cookies)
        
        def helper(i):
            nonlocal ans,fair
            if i==n:
                ans=min(ans,max(fair))
                return
            
            if max(fair)>=ans:
                return
            
            for j in range(k):
                fair[j]+=cookies[i]
                helper(i+1)
                fair[j]-=cookies[i]
            
        helper(0)
        return ans