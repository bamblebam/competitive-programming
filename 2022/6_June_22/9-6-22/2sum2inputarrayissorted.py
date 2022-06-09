class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for each number use binary search to check if target-num exists or not
        """
        n=len(nums)
        
        def binary_search(left,right,target):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    return mid
            return None
        
        ans=None
        for i,num in enumerate(nums):
            x=binary_search(i+1,n-1,target-num)
            if x != None:
                ans=[i+1,x+1]
                break
        
        return ans