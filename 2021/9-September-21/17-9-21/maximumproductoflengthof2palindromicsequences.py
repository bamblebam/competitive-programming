# O(3^n) solution, backtracking
class Solution:
    def maxProduct(self, s: str) -> int:
        n=len(s)
        ans=0
        def helper(idx,a,b):
            if idx==n:
                nonlocal ans
                if len(a)*len(b)>ans:
                    if a==a[::-1] and b==b[::-1]:
                        ans=len(a)*len(b)
                return
            helper(idx+1,a,b)
            a.append(s[idx])
            helper(idx+1,a,b)
            a.pop()
            b.append(s[idx])
            helper(idx+1,a,b)
            b.pop()
        helper(0,list(),list())
        return ans