class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        count=1
        seen=set()
        while i<len(nums):
            if nums[i] in seen:
                break
            if nums[i]!=nums[i-1]:
                count=1
                seen.add(nums[i-1])
            if nums[i]==nums[i-1]:
                count+=1
            if count>2:
                x=nums.pop(i)
                i-=1
            i+=1
        return len(nums)