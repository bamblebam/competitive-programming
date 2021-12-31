class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #use graphs and indegrees(prerequisites)
        #for all relations make a dict to store the parent child relation also update the prerequisite array to keep track of the courses that need to be done
        #put all courses that dont have prerequisites into min heap on basis of time
        #pop element from heap then iterate over all its children and reduce the prerequisite count
        #if child has 0 prerequisites add it to the heap with its time + parents time since that is the earliest that course can be done
        #return the first time when all courses are complete
        prerequisites=[0]*n
        edges=defaultdict(list)
        for u,v in relations:
            u-=1
            v-=1
            prerequisites[v]+=1
            edges[u].append(v)
        h=list()
        for course in range(n):
            if prerequisites[course]==0:
                heapq.heappush(h,(time[course],course))
                
        completed=0
        while h:
            t,course=heapq.heappop(h)
            completed+=1
            if completed==n:
                return t
            for nxtCourse in edges[course]:
                prerequisites[nxtCourse]-=1
                if prerequisites[nxtCourse]==0:
                    print(course,nxtCourse,t)
                    heapq.heappush(h,(t+time[nxtCourse],nxtCourse))
                    
        return t