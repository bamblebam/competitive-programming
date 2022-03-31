class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        remove all L from left and R from right
        then the total number of collisions will be the remaining moving cars
        """
        queue=deque(directions)
        
        while queue and queue[0]=='L':
            queue.popleft()
        
        while queue and queue[-1]=='R':
            queue.pop()
        
        return len(queue)-queue.count('S')