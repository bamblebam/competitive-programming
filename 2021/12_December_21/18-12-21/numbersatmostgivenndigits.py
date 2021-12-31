class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        #use dp
        #check for each number that is smaller than n and check if it only has digits from d
        #go through the length of n and then through each digit check if it is smaller than that of n if yes add all its permutations if it is equal then take the permutations of all nums smaller than it .ie. dp[i+1]
        s=str(n)
        k=len(s)
        dp=[0]*k+[1]
        
        for i in range(k-1,-1,-1):
            for d in digits:
                if d<s[i]:
                    dp[i]+=len(digits)**(k-i-1)
                elif d==s[i]:
                    dp[i]+=dp[i+1]
        
        return dp[0]+sum([len(digits)**i for i in range(1,k)]) #second part of this takes care of all the nums that have less digits than n