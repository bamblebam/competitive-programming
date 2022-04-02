class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        l,r=0,n-1
        while l<=r:
            if s[l]!=s[r]:
                break
            l+=1
            r-=1
        
        def helper(s):
            n=len(s)
            l,r=0,n-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        word1=s[:l]+s[l+1:]
        word2=s[:r]+s[r+1:]
        
        if any([helper(s),helper(word1),helper(word2)]):
            return True
        return False