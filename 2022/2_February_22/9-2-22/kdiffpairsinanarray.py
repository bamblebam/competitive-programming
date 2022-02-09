class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            count=Counter(nums)
            ans=0
            for k,v in count.items():
                if v>=2:
                    ans+=1
            return ans
        ans=0
        count=Counter()
        n=len(nums)
        seen=set()
        nums2=list()
        for i in range(n-1,-1,-1):
            if nums[i] in seen:
                continue
            nums2.append(nums[i])
            seen.add(nums[i])
        nums=nums2
        n=len(nums)
        for j in range(n):
            ans+=count[k+nums[j]]
            ans+=count[nums[j]-k]
            count[nums[j]]+=1
        return ans