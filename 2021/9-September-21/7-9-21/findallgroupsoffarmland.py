# iterate through the land matrix until you find a 1 then go down the column until you find a 0
# then go right in the row until you find a 0. Then you have the leftmost and rightmost coords
# after that just convert all the ones in the box formed by those coords to 0, and add the coords to the ans

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        ans = list()

        temp = list()
        for x in range(rows):
            for y in range(cols):
                if land[x][y] == 1:
                    # land[x][y]=0
                    temp.extend([x, y])
                    for dx in range(x, rows+1):
                        # if land[dx][y]==1:
                        #     land[dx][y]=0
                        #     continue
                        if dx >= rows or dx < 0 or land[dx][y] == 0:
                            break
                    dx -= 1
                    for dy in range(y, cols+1):
                        if dy >= cols or dy < 0 or land[dx][dy] == 0:
                            break
                    dy -= 1
                    temp.extend([dx, dy])
                    for i in range(x, dx+1):
                        for j in range(y, dy+1):
                            land[i][j] = 0
                    ans.append(temp)
                    temp = list()

        return ans
