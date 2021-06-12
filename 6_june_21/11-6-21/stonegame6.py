class Solution:
    def stoneGameVI(self, aliceValues, bobValues) -> int:
        n = len(aliceValues)
        diff_arr = sorted(
            [(i+j, idx) for idx, (i, j) in enumerate(zip(aliceValues, bobValues))])
        a = b = 0
        while diff_arr:
            a_idx = diff_arr[-1][1]
            a += aliceValues[a_idx]
            diff_arr.pop()
            if diff_arr:
                b_idx = diff_arr[-1][1]
                b += bobValues[b_idx]
                diff_arr.pop()
        score = a-b
        if score > 0:
            return 1
        elif score < 0:
            return -1
        else:
            return 0
