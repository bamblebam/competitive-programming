
# Correct but TLE
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = list()

        def helper(idx, arr):
            if idx == n:
                s = "".join(arr)
                if eval(s) == target:
                    ans.append(s)
                return

            arr.append('+')
            arr.append(num[idx])
            helper(idx+1, arr)
            arr.pop()
            arr.pop()

            arr.append('-')
            arr.append(num[idx])
            helper(idx+1, arr)
            arr.pop()
            arr.pop()

            arr.append('*')
            arr.append(num[idx])
            helper(idx+1, arr)
            arr.pop()
            arr.pop()

            prev = arr[-1]
            if arr[-1] != '0':
                arr[-1] += num[idx]
                helper(idx+1, arr)
                arr.pop()
                arr.append(prev)

        helper(1, [num[0]])
        return ans

# works
# class Solution:
#     def addOperators(self, num, target):
#         def dfs(idx, path, value, last):
#             if idx == n and value == target:
#                 ans.append(path)

#             for i in range(idx + 1, n + 1):
#                 tmp = int(num[idx: i])
#                 if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
#                     if last is None :
#                         dfs(i, num[idx: i], tmp, tmp)
#                     else:
#                         dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
#                         dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
#                         dfs(i, path + '*' + num[idx: i], value - last + last*tmp, last*tmp)

#         ans, n = [], len(num)
#         dfs(0, "", 0, None)
#         return ans
