class Solution:
    def merge(self, intervals):
        answers = list()
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not answers or answers[-1][1] < interval[0]:
                answers.append(interval)
            else:
                answers[-1][1] = max(interval[1], answers[-1][1])
        return answers


sol = Solution()
print(sol.merge([[2, 3], [4, 6], [5, 7], [3, 4]]))
