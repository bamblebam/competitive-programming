class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        for palindrome only find first half of string then reverse it and append it to itself
        adding x to the base will give you the xth palindrome
        """
        n=(intLength+1)//2-1
        def helper(x):
            x-=1
            s=str(10**n+x)
            if intLength%2:
                return s+s[::-1][1:]
            return s+s[::-1]
        
        ans=list()
        for q in queries:
            r=helper(q)
            if len(r)!=intLength:
                ans.append(-1)
            else:
                ans.append(int(r))
        
        return ans
                