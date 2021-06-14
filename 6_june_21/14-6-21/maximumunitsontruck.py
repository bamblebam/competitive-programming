class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for amt, units in boxTypes:
            cnt = min(truckSize, amt)
            ans += (cnt*units)
            truckSize -= cnt
            if truckSize == 0:
                break
        return ans
