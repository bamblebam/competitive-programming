class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=list()
        even=list()
        n=len(nums)
        for i in range(n):
            if i%2:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        odd.sort()
        even.sort(reverse=True)
        ans=list()
        for i in range(n):
            if i%2:
                ans.append(odd.pop())
            else:
                ans.append(even.pop())
        return ans