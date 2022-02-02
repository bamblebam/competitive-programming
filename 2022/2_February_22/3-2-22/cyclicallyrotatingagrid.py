class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #just go around the array in layers, store stuff in temp arr and reassign them
        m,n=len(grid),len(grid[0])
        ll=min(m,n)//2
        for l in range(ll):
            temp=list()
            for i in range(l,n-l-1): #top
                temp.append(grid[l][i])
            
            for i in range(l,m-l-1):#right
                temp.append(grid[i][n-l-1])
            
            for i in range(n-l-1,l,-1):#bottom
                temp.append(grid[m-l-1][i])
            
            for i in range(m-l-1,l,-1):#left
                temp.append(grid[i][l])
            
            v=len(temp)
            start=k%v
            
            for i in range(l,n-l-1): #top
                grid[l][i]=temp[start%v]
                start+=1
            
            for i in range(l,m-l-1):#right
                grid[i][n-l-1]=temp[start%v]
                start+=1
            
            for i in range(n-l-1,l,-1):#bottom
                grid[m-l-1][i]=temp[start%v]
                start+=1
            
            for i in range(m-l-1,l,-1):#left
                grid[i][l]=temp[start%v]
                start+=1
            
        return grid
            