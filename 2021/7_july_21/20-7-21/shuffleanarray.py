import random
class Solution:

    def __init__(self, nums):
        self.nums=nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        nums2=self.nums.copy()
        random.shuffle(nums2)
        return nums2


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()