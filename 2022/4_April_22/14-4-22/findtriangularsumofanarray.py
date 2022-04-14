class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newNums=list()
        i=0
        n=len(nums)
        while len(nums)>1:
            newNums.append((nums[i]+nums[i+1])%10)
            i+=1
            if i==n-1:
                i=0
                n=len(newNums)
                nums=newNums[:]
                newNums=list()
        return nums[0]