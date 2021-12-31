class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #2sum approach where target=60
        #go through all nums and add the num of pairs of it and its complement .ie. 1->59, 2->58
        #update the dp arr where the counts of all the modulo are stored
        ans=0
        dp=[0]*60
        for num in time:
            ans+=dp[-num%60]
            dp[num%60]+=1
        return ans