class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        nums=arr
        n=len(nums)
        if k>n:
            return 0
        count=0
        ans=0
        for i in range(n):
            num=nums[i]
            count+=num
            if i>=k-1:
                if count//k>=threshold:
                    ans+=1
                count-=nums[i-k+1]
        return ans