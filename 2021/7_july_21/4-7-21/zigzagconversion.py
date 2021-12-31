class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        dp = dict()
        for i in range(numRows):
            dp[i] = list()
        i = 0
        while i < n:
            down = 0
            while down <= numRows-1:
                if i >= n:
                    break
                dp[down].append(s[i])
                down += 1
                i += 1
            up = numRows-2
            while up > 0:
                if i >= n:
                    break
                dp[up].append(s[i])
                up -= 1
                i += 1
        newlist = list()
        for key, item in dp.items():
            newlist.extend(item)
        return "".join(newlist)
