class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        greedy approach
        fill the first space with the smallest letter and check if the other spaces can fulfill the request
        if not increment the letter
        do this for all n spaces
        """
        ans=list()
        for i in range(n):
            left=n-i-1
            for c in range(26):
                if (c+1)+left*26>=k:
                    ans.append(chr(c+ord('a')))
                    k-=(c+1)
                    break
        return "".join(ans)