class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count=Counter(tasks)
        ans=0
        for k,v in count.items():
            if v==1:
                return -1
            if v%3==0:
                ans+=v//3
            elif v%3==1:
                ans+=v//3-1+2
            else:
                ans+=v//3+1
        return ans
            