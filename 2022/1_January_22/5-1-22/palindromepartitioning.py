class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #get all palindromes and backtrack
        #check whether a substring is a palindrome
        #use backtracking to add them to ans
        
        n=len(s)
        is_palindrome=[[False]*n for _ in range(n)]
        for l in range(n):
            for r in range(l,n):
                curr=s[l:r+1]
                if curr==curr[::-1]:
                    is_palindrome[l][r]=True
        
        ans=list()
        def helper(curr,arr):
            if curr==n:
                ans.append(arr[:])
                return
            for r in range(curr,n):
                if is_palindrome[curr][r]:
                    arr.append(s[curr:r+1])
                    helper(r+1,arr)
                    arr.pop()
        
        helper(0,list())
        return ans