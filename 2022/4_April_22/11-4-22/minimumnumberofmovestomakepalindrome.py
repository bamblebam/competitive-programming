class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        use greedy solution using 2 pointers
        start from the left of the arr if you find a letter start from the back and find its first occurence
        the diff from the curr to the right will be the number of swaps needed
        keep on doing this until l<r
        if there is a center element it will not have a pair, consider it as well
        """
        n=len(s)
        l,r=0,n-1
        swaps=0
        middle=None
        arr=list(s)
        
        while l<r:
            curr=r
            while arr[l]!=arr[curr]:
                curr-=1
            if curr!=l:
                for x in range(curr,r):
                    arr[x],arr[x+1]=arr[x+1],arr[x]
                    swaps+=1
            else:
                middle=l
                l+=1
                continue
            l+=1
            r-=1
        
        if middle is not None:
            assert(n%2==1)
            g=n//2
            swaps+=abs(middle-g)
        
        return swaps
        