class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """
        Let use dp with states dp(n, k), where it is (current index of pile, nubmer of elements we still need to take). Then on each state we can try to take 0, ..., min(k, len(piles[m])) elements from pile m. Also if n == N, that is we reached the last pile and k == 0, we are happy, return 0. If k > 0, it means that we reached the last pile and did not take k elements, we are not happy, return -inf.

Complexity
Imagine, that piles have x1, ..., xn elements in them. Then for state (1, k) we have x1 possible transactions, for state (2, k) we have x2 possible transactions and so on. In total we have x1 + ... + xn transactions for every value of k. So, in total we have time complexity O(M * K), where M = x1 + ... + xn. Space is O(n * K).
        """
        n=len(piles)
        @cache
        def dp(idx,k):
            if idx==n:
                if k==0:
                    return 0
                if k>0:
                    return float("-inf")
            cost=dp(idx+1,k)
            rcost=0
            for i in range(min(k,len(piles[idx]))):
                rcost+=piles[idx][i]
                cost=max(cost,rcost+dp(idx+1,k-i-1))
            return cost
        return dp(0,k)