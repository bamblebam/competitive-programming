class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        answer = 0
        while Y > X:
            answer += 1
            if Y % 2:
                Y += 1
            else:
                Y /= 2
        return int(answer+X-Y)


sol = Solution()
print(sol.brokenCalc(3, 10))
