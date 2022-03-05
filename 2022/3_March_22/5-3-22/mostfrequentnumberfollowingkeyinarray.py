class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count=Counter()
        n=len(nums)
        for i in range(n-1):
            if nums[i]==key:
                count[nums[i+1]]+=1
        maxK,maxV=0,0
        for k,v in count.items():
            if v>maxV:
                maxK=k
                maxV=v
        return maxK