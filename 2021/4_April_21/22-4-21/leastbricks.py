import collections


class Solution:
    def leastBricks(self, wall) -> int:
        freq_dict = collections.Counter()
        for row in wall:
            offset = 0
            for brick in row[:-1]:
                offset += brick
                freq_dict[offset] += 1
        if len(freq_dict) == 0:
            return len(wall)
        return len(wall)-max(freq_dict.values())
