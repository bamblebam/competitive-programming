from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        t=len(tasks)
        n=len(workers)
        tasks.sort(reverse=True)
        workers.sort(reverse=True)
        
        #check how many tasks can be done using binary search
        
        def helper(tasks,workers):
            curr=SortedList(workers)
            p=pills
            for task in tasks:
                if curr[-1]>=task: #if thw worker is stronger than the task renove him
                    curr.pop()
                    continue
                else:
                    if p==0: #no pill remaining so false
                        return False
                    p-=1
                    idx=curr.bisect_left(task-strength)
                    if idx>=len(curr): #no worker is strong enough to do the task even with pill so false
                        return False
                    curr.remove(curr[idx])
            return True
        
        l,r=0,min(t,n)
        while l<r:
            mid=(l+r+1)//2
            if helper(tasks[-mid:],workers[:mid]): #we take the easiest mid tasks and the strongest mid workers
                l=mid
            else:
                r=mid-1
        
        return l
        