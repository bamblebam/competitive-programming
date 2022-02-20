class Solution:
    def countEven(self, num: int) -> int:
        def digitSum(num):
            count=0
            while num>0:
                count+=num%10
                num//=10
            return count
        
        ans=0
        for i in range(1,num+1):
            if digitSum(i)%2==0:
                ans+=1
        return ans