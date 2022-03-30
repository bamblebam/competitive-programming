class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        can't understand shit
        something about searching in the rotated parts
        """
        def find(left,right):
            if left>right:
                return False
            if left==right:
                return nums[left]==target
            if left+1==right:
                return nums[left]==target or find(left+1,right)
            
            mid=(left+right)//2
            
            if nums[left]<nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    return find(left,mid)
                else:
                    return find(mid+1,right)
            elif nums[left]>nums[mid]:
                if nums[mid]<=target<=nums[right]:
                    return find(mid,right)
                else:
                    return find(left,mid-1)
            else:
                return find(left,mid-1) or find(mid,right)
            
        return find(0,len(nums)-1)