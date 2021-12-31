class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #go through the array and put elements in a monotone stack
        #if element is greater than prev element pop it
        stack=list()
        n=len(temperatures)
        ans=[0]*n
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                prevtemp,idx=stack.pop()
                ans[idx]=i-idx
            stack.append([temp,i])
        return ans