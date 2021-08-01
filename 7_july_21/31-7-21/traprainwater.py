class Solution:
    def trap(self, heights) -> int:
        total = 0
        n = len(heights)
        i = 0
        stack = list()
        while i < n:
            if not stack or heights[i] <= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                curr_idx = stack.pop()
                if stack:
                    min_height = min(heights[stack[-1]], heights[i])
                    total += (min_height-heights[curr_idx])*(i-stack[-1]-1)
        return total
