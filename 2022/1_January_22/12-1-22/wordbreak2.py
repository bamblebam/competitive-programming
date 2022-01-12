class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #use bfs like word break 1
        #add first idx and "" to queue then just popleft and go through the remaining indices
        #if they are in words append it to path and add it to queue
        #if end==n then the entire string is done so add it to ans
        #we dont use seen set to avoid repeat because for the same start we could have multiple following words
        #alt way is to take the list of all unique lengths of words in words and iterate over just them because those are the only valid indices where the path can end
        n=len(s)
        queue=deque([(0,"")])
        ans=list()
        words=set(wordDict)
        lenlist=set(map(len,wordDict))
         
        while queue:
            start,path=queue.popleft()
            for end in range(start+1,n+1):
                if s[start:end] in words:
                    new=(end,path+" "+s[start:end] if path else s[start:end])
                    queue.append(new)
                    if end==n:
                        ans.append(new[1])
        
        return ans
            
        
#         while queue:
#             start,path=queue.popleft()
#             for end in lenlist:
#                 if start+end<=n and s[start:start+end] in words:
#                     new=(start+end,path+" "+s[start:start+end] if path else s[start:start+end])
#                     queue.append(new)
#                     if start+end==n:
#                         ans.append(new[1])
#             seen.add(start)
        
#         return ans