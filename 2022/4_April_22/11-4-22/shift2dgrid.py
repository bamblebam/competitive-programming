class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Imagine the grid to be a 1-D array of size m * n;
reverse the whole array;
reverse the first k elements
reverse the remaing m * n - k element.
        """
        m,n=len(grid),len(grid[0])
        def helper(l,r):
            while l<r:
                x1,y1,x2,y2=l//n,l%n,r//n,r%n
                grid[x1][y1],grid[x2][y2]=grid[x2][y2],grid[x1][y1]
                l+=1
                r-=1
        
        k%=m*n
        helper(0,m*n-1)
        helper(0,k-1)
        helper(k,m*n-1)
        
        return grid