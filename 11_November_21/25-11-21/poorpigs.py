class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        #math (T+1)^x >=N
        return ceil(log(buckets)/log(minutesToTest//minutesToDie+1))