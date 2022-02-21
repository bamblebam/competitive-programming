class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=defaultdict(list)
        for i,x in enumerate(nums):
            count[x].append(i)
        ans=0
        for v in count.values():
            for i in range(len(v)):
                for j in range(i+1,len(v)):
                    if v[i]*v[j]%k==0:
                        ans+=1
        return ans