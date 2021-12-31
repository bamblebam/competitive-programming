class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        diff = 0
        n = len(keysPressed)
        d = (0, '')
        for i in range(n):
            t = releaseTimes[i]-diff
            print(t)
            diff = releaseTimes[i]
            if t > d[0]:
                d = (t, keysPressed[i])
            elif t == d[0] and d[1] < keysPressed[i]:
                d = (d[0], keysPressed[i])

        return d[1]
