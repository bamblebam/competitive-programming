class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #basic graph BFS
        #indegree is the number of prerequisites required for a particular course
        #completed keeps track of the number of courses completed
        if len(prerequisites)<=1:
            return True
        
        edges_map=defaultdict(set)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            edges_map[v].add(u)
            indegree[u]+=1
        
        queue=deque([i for i,x in enumerate(indegree) if x==0])
        completed=len(queue)
        
        while queue:
            course=queue.popleft()#check if all prerequisites are done if yes then put that course in the queue
            for v in edges_map[course]:
                indegree[v]-=1
                if indegree[v]==0:
                    completed+=1
                    queue.append(v)
                if completed==numCourses:
                    return True
        return False
        