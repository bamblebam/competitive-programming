class Solution:
    def generate(self, numRows: int):
        ans = list()
        prev = list()
        for i in range(numRows):
            temp = list()
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(prev[j]+prev[j-1])
            ans.append(temp)
            prev = temp
        return ans
