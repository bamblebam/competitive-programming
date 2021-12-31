# sort it in ascending of attack (x[0]) and descending of defense (x[1]) then traverse the array in reverse and check if the y is less than the greatest y if yes then increase count
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        mxy = -1
        for x, y in properties[::-1]:
            mxy = max(y, mxy)
            if mxy > y:
                count += 1
        return count
