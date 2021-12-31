class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        #it is a graph problem
        #put start in queue and the distance for it as 0
        #the popleft and check for all 3 possibilities
        #if any one is equal to goal return else add them to queue and dist
        n=len(nums)
        queue=deque([start])
        dist=dict()
        dist[start]=0
        
        while queue:
            curr=queue.popleft()
            for i in range(n):
                
                cands=[curr+nums[i],curr-nums[i],curr^nums[i]]
                
                for cand in cands:
                    if cand==goal:
                        return dist[curr]+1
                
                for cand in cands:
                    if 0<=cand<=1000 and cand not in dist:
                        queue.append(cand)
                        dist[cand]=dist[curr]+1
        
        return -1
                        
                
                
            