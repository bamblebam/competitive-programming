class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        newnums=list()
        while len(nums)>1:
            n=len(nums)
            for i in range(n//2):
                if i%2:
                    newnums.append(max(nums[2*i],nums[2*i+1]))
                else:
                    newnums.append(min(nums[2*i],nums[2*i+1]))
            nums=newnums[:]
            newnums=list()
        return nums[0]