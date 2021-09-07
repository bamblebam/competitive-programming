class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum, right_sum = [0], [0]

        for x in nums[::-1]:
            right_sum.append(right_sum[-1]+x)
        right_sum.reverse()

        for x in nums:
            left_sum.append(left_sum[-1]+x)

        for i, (a, b) in enumerate(zip(left_sum[1:], right_sum[:-1])):
            if a == b:
                return i
        print(left_sum, right_sum)
        return -1
