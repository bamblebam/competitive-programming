class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses<2 or not prerequisites:
            return list(range(numCourses))
        
        edges_map=defaultdict(set)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            edges_map[v].add(u)
            indegree[u]+=1
        
        queue=deque([i for i,x in enumerate(indegree) if x==0])
        completed=len(queue)
        ans=list()

        while queue:
            course=queue.popleft()
            ans.append(course)
            for v in edges_map[course]:
                indegree[v]-=1
                if indegree[v]==0:
                    completed+=1
                    queue.append(v)
        
        if completed==numCourses:
            return ans
        return list()