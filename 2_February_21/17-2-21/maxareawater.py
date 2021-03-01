class Solution:
    def maxArea(self, height):
        l = len(height)-1
        f = 0
        area = 0
        while f < l:
            area = max(area, min(height[f], height[l])*abs(f-l))
            if height[f] > height[l]:
                l = l-1
            else:
                f = f+1
        return area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
