class Solution:
    def racecar(self, target: int) -> int:
        """
        https://leetcode.com/problems/race-car/discuss/762584/Python-C%2B%2B-3-Simple-Steps-(BFS)
        """
        queue=deque([(0,0,1)])
        while queue:
            moves,pos,vel=queue.popleft()
            if pos==target:
                return moves
            queue.append((moves+1,pos+vel,vel*2))
            if (pos+vel>target and vel>0) or (pos+vel<target and vel<0):
                queue.append((moves+1,pos,-vel/abs(vel)))
            