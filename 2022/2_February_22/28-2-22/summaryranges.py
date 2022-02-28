class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans=list()
        temp=list()
        for i in range(len(nums)):
            if not temp:
                temp.append(nums[i])
                continue
            if nums[i]-nums[i-1]==1:
                temp.append(nums[i])
                continue
            if len(temp)>=2:
                ans.append(f"{temp[0]}->{temp[-1]}")
            else:
                ans.append(str(temp[0]))
            temp=[nums[i]]
        if len(temp)>=2:
            ans.append(f"{temp[0]}->{temp[-1]}")
        else:
            ans.append(str(temp[0]))
        return ans