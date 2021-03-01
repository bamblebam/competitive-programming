class Solution:
    def numberOfArithmeticSlices(self, A):
        length = len(A)
        sum = 0
        count = 0
        for i in range(2, length):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                count += 1
            else:
                sum += count*(count+1)/2
                count = 0
        sum += count*(count+1)/2
        return int(sum)


sol = Solution()
print(sol.numberOfArithmeticSlices([1, 2, 3]))
