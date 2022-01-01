class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #use dp to keep track of the longest chain that can be formed ending at a specific word
        dp=defaultdict(lambda:0)
        for word in sorted(words,key=len):
            for i in range(len(word)):
                prev=word[:i]+word[i+1:]
                dp[word]=max(dp[word],dp[prev]+1)
        return max(dp.values())
            