import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        counter = collections.Counter(s)
        res = [0]*10
        res[0] = counter['z']
        res[2] = counter['w']
        res[4] = counter['u']
        res[6] = counter['x']
        res[8] = counter['g']
        res[1] = counter['o']-res[0]-res[2]-res[4]
        res[3] = counter['h']-res[8]
        res[5] = counter['f']-res[4]
        res[7] = counter['s']-res[6]
        res[9] = counter['i']-res[5]-res[6]-res[8]
        return "".join(str(i)*f for i, f in enumerate(res))


sol = Solution()
print(sol.originalDigits("owoztneoer"))
