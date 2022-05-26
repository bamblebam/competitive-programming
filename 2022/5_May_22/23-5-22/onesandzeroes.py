class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        use dp to keep track of the number of zeroes and ones covered till now
        """
        pairs=[[s.count('0'),s.count('1')] for s in strs]
        
        @lru_cache(None)
        def dp(left_zero,left_ones,length_covered):
            if left_zero<0 or left_ones<0:
                return float('-inf')
            if length_covered>=len(strs):
                return 0
            zeroes,ones=pairs[length_covered]
            return max(dp(left_zero-zeroes,left_ones-ones,length_covered+1)+1,dp(left_zero,left_ones,length_covered+1))
        
        return dp(m,n,0)