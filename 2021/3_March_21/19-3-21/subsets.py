class Solution:
    answers = list()

    def helper(self, nums, path, first, length):
        if len(path) == length:
            self.answers.append(path[:])
            return
        for i in range(first, len(nums)):
            path.append(nums[i])
            self.helper(nums, path, i+1, length)
            path.pop()

    def subsets(self, nums):
        self.answers = list()
        for k in range(len(nums)+1):
            self.helper(nums, [], 0, k)
        return self.answers


sol = Solution()
print(sol.subsets([1, 2, 3]))
