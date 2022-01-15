class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        seen=set()
        n=len(s)
        idx_map=[i for i,c in enumerate(s) if c=="0"]
        queue=deque([idx_map[0]])
        
        while queue:
            curr=queue.popleft()
            if curr==n-1:
                return True
            left=bisect_left(idx_map,curr+minJump)
            right=bisect_right(idx_map,curr+maxJump)
            temp=list()
            for x in idx_map[left:right]:
                if x in seen:
                    continue
                seen.add(x)
                queue.append(x)
                temp.append(x)
            for x in temp:
                idx_map.remove(x)
        
        return False