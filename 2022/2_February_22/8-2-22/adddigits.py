class Solution:
    def addDigits(self, num: int) -> int:
        def helper(num):
            ans=0
            while num:
                ans+=num%10
                num//=10
            if ans<10:
                return ans
            else:
                ans=helper(ans)
            return ans
        return helper(num)