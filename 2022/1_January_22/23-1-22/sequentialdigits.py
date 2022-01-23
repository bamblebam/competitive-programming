class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #use backtracking sorta?
        ans=set()
        
        def helper(num):
            nonlocal ans
            x=int(num)
            if low<=x<=high:
                ans.add(x)
            if x>high:
                return
            y=int(num[-1])+1
            if y>9:
                return
            helper(num+str(y))
            
        for i in range(1,10):
            helper(str(i))
            
        return sorted(ans)