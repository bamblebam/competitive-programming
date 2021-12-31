class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #use bfs 
        #put the start in queue and seen set then just pop it and check if the left and right jump indices exist
        #if they do put them in the queue and set
        #continue this till we get an idx which has 0 or return False
        n=len(arr)
        queue=deque([start])
        seen={start}
        
        while queue:
            idx=queue.popleft()
            left_jump=idx-arr[idx]
            right_jump=idx+arr[idx]
            
            if arr[idx]==0:
                return True
            
            if 0<=left_jump<n and left_jump not in seen:
                queue.append(left_jump)
                seen.add(left_jump)
                
            if 0<=right_jump<n and right_jump not in seen:
                queue.append(right_jump)
                seen.add(right_jump)
        
        return False