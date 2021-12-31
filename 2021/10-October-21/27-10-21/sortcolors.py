class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #dutch national flag problem
        n=len(nums)
        l,r=0,n-1 #idx just after the last 0 or idx just before the first 2
        i=0 #curr idx or idx just after the last 1
        while i<=r:
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            else:
                i+=1