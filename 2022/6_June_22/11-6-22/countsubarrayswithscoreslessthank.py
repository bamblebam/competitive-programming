class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        """
        make a prefix array to calculate the sum of a subarray in constant time
        then use 2 pointer with for loop and increment the ans where necessary
        """
        
        prefix=[0]+list(accumulate(nums))
        ans=0
        n=len(nums)
        ans=0
        
        left=0
        
        for i in range(n):
            right=i+1
            if left>right:
                break
            length=right-left
            sum_=prefix[right]-prefix[left]
            while length*sum_>=k:
                left+=1
                if left>right:
                    break
                length=right-left
                sum_=prefix[right]-prefix[left]
            ans+=length
                
        return ans
   