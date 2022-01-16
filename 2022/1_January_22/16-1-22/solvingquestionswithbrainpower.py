class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #use recursive dp
        #at each point you can have 2 decisions
        #solve the question and then solve the question brainpower steps away or
        #don't solve the question and do the next one
        n=len(questions)
        
        @lru_cache(None)
        def helper(idx):
            if idx>=n:
                return 0
            best=0
            best=max(best,helper(idx+1))#don't solve the question and do the next one
            best=max(best,questions[idx][0]+helper(idx+questions[idx][1]+1))#solve the question and then solve the question brainpower steps away 
            
            return best
        
        return helper(0)
            