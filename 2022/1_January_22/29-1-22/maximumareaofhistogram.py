class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #same like maximal rectangle
        #use a monotonic increasing stack
        #when you get a smaller num pop it and take area of previous rectangles
        ans=0
        stack=list()
        n=len(heights)
        for i,h in enumerate(heights+[0]):
            while stack and heights[stack[-1]]>=h:
                hgt=heights[stack.pop()]
                wth=i if not stack else i-stack[-1]-1
                ans=max(ans,hgt*wth)
            stack.append(i)
        return ans