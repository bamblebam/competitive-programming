class Solution:
    def queensAttacktheKing(self, queens, king):
        ans = set()
        queens2 = set()
        for queen in queens:
            x, y = queen
            queens2.add((x, y))
        queens = queens2
        x, y = king
        temp_x, temp_y = x, y
        # forward
        temp_x, temp_y = x, y
        while temp_x < 8:
            if (temp_x, y) in queens:
                ans.add((temp_x, y))
                break
            temp_x += 1
        # backward
        temp_x, temp_y = x, y
        while temp_x >= 0:
            if (temp_x, y) in queens:
                ans.add((temp_x, y))
                break
            temp_x -= 1
        # right
        temp_x, temp_y = x, y
        while temp_y < 8:
            if (x, temp_y) in queens:
                ans.add((x, temp_y))
                break
            temp_y += 1
        # left
        temp_x, temp_y = x, y
        while temp_y >= 0:
            if (x, temp_y) in queens:
                ans.add((x, temp_y))
                break
            temp_y -= 1
        # upper-right
        temp_x, temp_y = x, y
        while temp_y >= 0 and temp_x < 8:
            if (temp_x, temp_y) in queens:
                ans.add((temp_x, temp_y))
                break
            temp_y -= 1
            temp_x += 1
        # upper-left
        temp_x, temp_y = x, y
        while temp_y >= 0 and temp_x >= 0:
            if (temp_x, temp_y) in queens:
                ans.add((temp_x, temp_y))
                break
            temp_y -= 1
            temp_x -= 1
        # lower-right
        temp_x, temp_y = x, y
        while temp_y < 8 and temp_x < 8:
            if (temp_x, temp_y) in queens:
                ans.add((temp_x, temp_y))
                break
            temp_y += 1
            temp_x += 1
        # lower-left
        temp_x, temp_y = x, y
        while temp_y < 8 and temp_x >= 0:
            if (temp_x, temp_y) in queens:
                ans.add((temp_x, temp_y))
                break
            temp_y += 1
            temp_x -= 1
        return ans
