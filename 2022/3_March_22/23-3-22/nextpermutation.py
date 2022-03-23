class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        traverse the array from right and find the first decreasing pair where a[i]<a[i+1]
        that is i
        then treverse left from that element to the end and find the next largest element that is j
        swap i and j
        reverse the array from i to end
        """
        n=len(nums)
        flag=False
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                flag=True
                break

        if not flag:
            nums.sort()
        else:
            justLarger=float('inf')
            justLargeridx=-1
            for j in range(i+1,n):
                if nums[j]>nums[i] and nums[j]<=justLarger:
                    justLarger=nums[j]
                    justLargeridx=j

            nums[i],nums[justLargeridx]=nums[justLargeridx],nums[i]
            i+=1
            r=n-1
            while i<r:
                nums[i],nums[r]=nums[r],nums[i]
                i+=1
                r-=1
        