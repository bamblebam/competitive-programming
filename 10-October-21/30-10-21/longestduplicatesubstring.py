class Solution:
    def longestDupSubstring(self, s: str) -> str:
        #use binary search to find the max length of the substring which can be repeated.
        #for the particular length put all substrings of that length into a counter
        #check if any substring occurs 2 or more times if it does the max length is greater than what we have selected so increase l
        #else decrease r because the length is less than what we selected
        #TC = O(n*log(n))
        #if we do bruteforce way of taking all substrings of a specific length for all lengths TC will be O(n^2)
        n=len(s)
        l,r=0,n-1
        ans=""
        while l<=r:
            mid=(l+r)//2
            count=Counter()
            istwo=False
            for i in range(n-mid+1):
                x=s[i:i+mid]
                count[x]+=1
                if count[x]>=2:
                    istwo=True
                    ans=x
                    break
            if istwo:
                l=mid+1
            else:
                r=mid-1
        return ans