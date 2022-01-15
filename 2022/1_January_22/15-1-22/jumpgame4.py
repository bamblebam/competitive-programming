class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #use bfs, dp doesn't work
        #treat the array like a graph
        #add elems in a queue sequentially and check if we have reached the last idx, if yes then return the number of steps
        #also create dict to store indices of all same nums
        n=len(arr)
        idx_map=defaultdict(list)
        for i,x in enumerate(arr):
            idx_map[x].append(i)
        
        queue=deque([(0,0)])
        seen=set()
        
        while queue:
            steps,curr=queue.popleft()
            if curr==n-1:
                return steps
            
            for neib in [curr+1,curr-1]:
                if 0<=neib<n and neib not in seen:
                    queue.append((steps+1,neib))
                    seen.add(neib)
            
            for neib in idx_map[arr[curr]]:
                if curr!=neib and neib not in seen:
                    queue.append((steps+1,neib))
                    seen.add(neib)
            idx_map[arr[curr]]=list()
            
                    