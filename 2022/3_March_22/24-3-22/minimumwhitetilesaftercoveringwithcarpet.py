class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """
        use dp
        dp(idx,left) is the minimum number of 1s before idx by using left number of carpets
        """
        @cache
        def dp(idx,left):
            if left<0:
                return float('inf')
            if idx<0:
                return 0
            return min(dp(idx-carpetLen,left-1),dp(idx-1,left)+int(floor[idx]))
        return dp(len(floor)-1,numCarpets)