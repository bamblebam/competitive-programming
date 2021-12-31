class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        n = len(bits)
        ans = 0
        i = 0
        while i < n:
            if bits[i] == 0:
                i += 1
                ans = 0
            else:
                i += 2
                ans = 1
        return not ans
