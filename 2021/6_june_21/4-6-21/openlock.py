from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        queue1, queue2 = deque([(0, '0000')]), deque([(0, target)])
        visited1, visited2 = {'0000': 0}, {target: 0}
        limit, ans = float('inf'), float('inf')
        while queue1:
            if len(queue1) > len(queue2):
                queue2, queue1 = queue1, queue2
                visited1, visited2 = visited2, visited1
            steps, code = queue1.popleft()
            if steps + queue2[0][0] > limit:
                return ans
            if code in visited2:
                limit = steps+queue2[0][0]
                ans = min(ans, visited1[code] + visited2[code])
            for i in range(4):
                d = int(code[i])
                for k in (d-1) % 10, (d+1) % 10:
                    cand = code[:i]+str(k)+code[i+1:]
                    if cand not in dead and cand not in visited1:
                        visited1[cand] = steps+1
                        queue1.append((steps+1, cand))
        return -1
