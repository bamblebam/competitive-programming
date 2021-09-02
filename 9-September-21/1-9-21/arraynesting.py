class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        nums_map = defaultdict(lambda: 0)
        for num in nums:
            count = set()
            n = num
            if n in nums_map:
                mx = max(mx, nums_map[n])
                continue
            while n not in count:
                if n in nums_map:
                    mx = max(mx, nums_map[n]+len(count))
                    break
                count.add(n)
                nums_map[n] = max(nums_map[n], len(count))
                n = nums[n]
            mx = max(mx, len(count))
        return mx
