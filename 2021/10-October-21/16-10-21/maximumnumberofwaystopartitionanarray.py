class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total=sum(nums)
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        suffix=[total-x for x in prefix]
        delta=[x-y for x,y in zip(prefix,suffix)]
        
        ans=0
        #for unchanged case
        for i in delta[1:-1]:
            if i==0:
                ans+=1
        #the freq of each element since we only want to know how many times it appears
        left=Counter()
        right=Counter(delta[1:-1])
        
        for i,x in enumerate(delta[1:]):
            diff=nums[i]-k
            ans=max(ans,left[-diff]+right[diff]) #number of elements to which when we add diff it becomes 0, left we take -ve because we add, right we take +ve cause we subtract
            left[x]+=1
            right[x]-=1
        
        return ans
        