class Solution:
    def removeBoxes(self, boxes) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0
            m = i+1
            count = 1
            # count the number of consecutive boxes
            while m <= j and boxes[m] == boxes[i]:
                count += 1
                m += 1
            # option 1: we takie the left group of nums
            ans = dp(m, j, 0)+(count+k)**2
            # option 2: we get rid of the middle nums to add the left and right grp of nums for larger num
            for n in range(m, j+1):
                if boxes[n] == boxes[i]:
                    ans = max(ans, dp(m, n-1, 0)+dp(n, j, k+count))
            return ans
        return dp(0, len(boxes)-1, 0)
