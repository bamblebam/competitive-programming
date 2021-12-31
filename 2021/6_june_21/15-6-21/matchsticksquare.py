class Solution:
    def makesquare(self, matchsticks) -> bool:
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        side_len = perimeter//4
        if side_len*4 != perimeter:
            return False
        sides = [0]*4

        def dfs(index):
            if index == n:
                return sides[0] == sides[1] == sides[2] == side_len
            for i in range(4):
                if sides[i]+matchsticks[index] <= side_len:
                    sides[i] += matchsticks[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= matchsticks[index]
            return False
        return dfs(0)
