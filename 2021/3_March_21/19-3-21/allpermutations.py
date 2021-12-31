class Solution:
    def __init__(self):
        self.answers = list()

    def helper(self, nums, path):
        if len(path) == len(nums):
            self.answers.append(path[:])
            return
        for i in nums:
            if i not in path:
                path.append(i)
                print(path)
                self.helper(nums, path)
                path.pop()

    def permute(self, nums):
        if len(nums) == 0:
            self.answers
        self.helper(nums, [])
        return self.answers


sol = Solution()
print(sol.permute([1, 2, 3]))
