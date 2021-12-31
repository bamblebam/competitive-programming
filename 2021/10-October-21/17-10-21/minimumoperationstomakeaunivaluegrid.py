class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #consider the median and try to get all numbers to that
        m=len(grid)
        n=len(grid[0])
        if m==1 and n==1:
            return 0
        arr=list()
        for i in range(m):
            arr.extend(grid[i])
        arr.sort()
        cand1=arr[len(arr)//2]
        cand2=arr[len(arr)//2-1]
        
        def helper(cand):
            ans=0
            for num in arr:
                if abs(num-cand)%x:
                    return -1
                else:
                    ans+= abs(num-cand)//x
            return ans
        
        return min(helper(cand1),helper(cand2))
        