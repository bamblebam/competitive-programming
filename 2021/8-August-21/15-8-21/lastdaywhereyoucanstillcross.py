# Union Find from left to right to form a wall
class Solution:
    def latestDayToCross(self, row: int, col: int, cells) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (-1, -1), (-1, 1), (1, -1)]
        parents = dict()
        seen = set()

        def ufind(key):
            if parents[key] != key:
                parents[key] = ufind(parents[key])
            return parents[key]

        def uunion(a, b):
            a = ufind(a)
            b = ufind(b)
            parents[a] = b

        for x in range(row):
            for y in range(col):
                parents[(x, y)] = (x, y)
        left, right = -1, -2
        parents[left], parents[right] = left, right

        for t, (x, y) in enumerate(cells):
            x -= 1
            y -= 1
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0 <= nx < row:
                    if 0 <= ny < col:
                        if (nx, ny) in seen:
                            uunion((x, y), (nx, ny))
                    else:
                        if ny == -1:
                            uunion((x, y), left)
                        elif ny == col:
                            uunion((x, y), right)
                if ufind(left) == ufind(right):
                    return t
                seen.add((x, y))
        return t


# Correct but TLE
# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells) -> int:
#         matrix = [[0]*col for _ in range(row)]
#         dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         ans = 0
#         global flag
#         flag = False
#         seen = set()

#         def dfs(x, y):
#             global flag
#             if x == row-1:
#                 flag = True
#             for dx, dy in dirs:
#                 nx, ny = dx+x, dy+y
#                 if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in seen and matrix[nx][ny] == 0:
#                     if nx == row-1:
#                         flag = True
#                     seen.add((nx, ny))
#                     dfs(nx, ny)

#         for i, j in cells:
#             matrix[i-1][j-1] = 1
#             flag = False
#             for k in range(col):
#                 if matrix[0][k] != 0:
#                     continue
#                 seen = set()
#                 seen.add((0, k))
#                 dfs(0, k)
#                 if flag:
#                     ans += 1
#                     break
#             if not flag:
#                 break

#         return ans
