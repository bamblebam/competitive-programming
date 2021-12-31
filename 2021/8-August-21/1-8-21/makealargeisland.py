# done via components split it into groups of 1's and  assign each group an id then get the area.
class Solution:
    def largestIsland(self, grid) -> int:
        n = len(grid)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, grid_id):
            count = 1
            grid[x][y] = grid_id
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not 0 <= nx < n or not 0 <= ny < n or grid[nx][ny] != 1:
                    continue
                else:
                    count += dfs(nx, ny, grid_id)
            return count

        id_map = dict()

        def count_area(x, y):
            count = 1
            num_set = set()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not 0 <= nx < n or not 0 <= ny < n or grid[nx][ny] in num_set:
                    continue
                else:
                    num_set.add(grid[nx][ny])
                    count += id_map.get(grid[nx][ny], 0)
            return count

        grid_id = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, grid_id)
                    id_map[grid_id] = area
                    grid_id += 1

        max_area = id_map.get(2, 0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_area = max(max_area, count_area(i, j))

        return max_area

# correct solution but gives TLE
# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         max_area=0
#         flag=False
#         flag2=False

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]!=0:
#                     flag2=True
#                     break
#             if flag2:
#                 break

#         if not flag2:
#             return 1

#         dirs=[(0,1),(1,0),(0,-1),(-1,0)]
#         seen=[[False]*n for _ in range(n)]

#         def dfs(x,y):
#             count=0
#             seen[x][y]=True
#             for dx,dy in dirs:
#                 nx,ny=x+dx,y+dy
#                 if not 0<=nx<n or not 0<=ny<n or seen[nx][ny] or grid[nx][ny]!=1:
#                     continue
#                 else:
#                     count+=dfs(nx,ny)+1
#             return count

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]==0:
#                     seen=[[False]*n for _ in range(n)]
#                     flag=True
#                     grid[i][j]=1
#                     max_area=max(max_area,dfs(i,j))
#                     grid[i][j]=0

#         if not flag:
#             return n**2

#         return max_area+1
