from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        get the indices of all the elements in num2 in a dict
        create list nums which has the idx of element in nums2 in the pos of nums1
        nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3] -> nums = [0,2,1,4,3]
        find all elements smaller to left and all elements greater to right for each element in nums
        ans is the sum of products
        """
        def smallerThanLeft(nums):
            n=len(nums)
            sl=SortedList()
            output=[0]*n
            for i in range(n):
                idx=sl.bisect_left(nums[i])
                sl.add(nums[i])
                output[i]=idx
            return output
        
        def greaterThanRight(nums):
            n=len(nums)
            sl=SortedList()
            output=[0]*n
            for i in range(n-1,-1,-1):
                idx=len(sl)-sl.bisect_left(nums[i])
                sl.add(nums[i])
                output[i]=idx
            return output
    
        n=len(nums1)
        nums_idx={nums2[i]:i for i in range(n)}
        nums=list()
        for num in nums1:
            nums.append(nums_idx[num])
        smaller=smallerThanLeft(nums)
        greater=greaterThanRight(nums)
        ans=0
        for a,b in zip(smaller,greater):
            ans+=a*b
        return ans
                