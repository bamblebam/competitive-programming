class Solution:
    def grayCode(self, n: int):
        def helper(result, n):
            if n == 0:
                result.append(0)
                return
            helper(result, n-1)
            curr_len = len(result)
            mask = 1 << (n-1)
            for i in range(curr_len-1, -1, -1):
                result.append(result[i] | mask)
        result = list()
        helper(result, n)
        return result
