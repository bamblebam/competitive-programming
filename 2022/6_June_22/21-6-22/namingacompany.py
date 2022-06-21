class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        """
        https://leetcode.com/problems/naming-a-company/discuss/2141038/Python-Explanation-with-pictures-group
        """
        initials=[set() for _ in range(26)]
        base=ord('a')
        
        for idea in ideas:
            initials[ord(idea[0])-base].add(idea[1:])
        
        ans=0
        for i in range(25):
            for j in range(i+1,26):
                k=len(initials[i]&initials[j])
                ans+=2*(len(initials[i])-k)*(len(initials[j])-k)
        
        return ans