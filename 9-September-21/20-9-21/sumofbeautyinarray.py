class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        min_elem = [0]
        for num in nums[:-1]:
            min_elem.append(max(num, min_elem[-1]))
        max_elem = [float('inf')]
        for num in reversed(nums):
            max_elem.append(min(max_elem[-1], num))
        max_elem.reverse()
        max_elem = max_elem[1:]

        count = 0
        for i in range(1, n-1):
            if min_elem[i] < nums[i] < max_elem[i]:
                count += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                count += 1

        return count
