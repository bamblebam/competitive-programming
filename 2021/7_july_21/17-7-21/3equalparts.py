class Solution:
    def threeEqualParts(self, arr):
        n = len(arr)
        arr = "".join(list(map(str, arr)))
        l, r = 0, n-1
        while l < r:
            left = int(arr[:l+1], 2)
            right = int(arr[r:], 2)
            if left == right:
                if l+1 == r:
                    return [-1, -1]
                mid = int(arr[l+1:r], 2)
                if left == right == mid:
                    return [l, r]
                r -= 1
            elif left > right:
                r -= 1
            else:
                l += 1
        return [-1, -1]
