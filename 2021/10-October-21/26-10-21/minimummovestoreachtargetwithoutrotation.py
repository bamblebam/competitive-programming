class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        #using bfs put the first point in list.
        #then pop it of and check for all 4 cases and if valid put those points in list and increase moves.
        n=len(grid)
        moves=0
        start=(0,0,0,1)
        end=(n-1,n-2,n-1,n-1)
        curr_level={start}
        visited=set()
        while curr_level:
            next_level=set()
            for pos in curr_level:
                r1,c1,r2,c2=pos
                visited.add(pos)
                #moving right
                if c1+1<n and c2+1<n and grid[r1][c1+1]==0 and grid[r2][c2+1]==0 and (r1,c1+1,r2,c2+1) not in visited:
                    next_level.add((r1,c1+1,r2,c2+1))
                #moving down
                if r1+1<n and r2+1<n and grid[r1+1][c1]==0 and grid[r2+1][c2]==0 and (r1+1,c1,r2+1,c2) not in visited:
                    next_level.add((r1+1,c1,r2+1,c2))
                #moving clockwise
                if r1==r2 and r2+1<n and grid[r2+1][c2]==0 and grid[r2+1][c1]==0 and (r1,c1,r2+1,c1) not in visited:
                    next_level.add((r1,c1,r2+1,c1))
                #moving anti clockwise
                if c1==c2 and c2+1<n and grid[r2][c1+1]==0 and grid[r1][c2+1]==0 and (r1,c1,r1,c2+1) not in visited:
                    next_level.add((r1,c1,r1,c2+1))
            if end in next_level:
                return moves+1
            curr_level=next_level
            moves+=1
        return -1