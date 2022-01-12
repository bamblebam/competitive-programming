class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #use bfs
        #add idx of first letter in queue then iterate over all the other indices and check if any word starting with idx exists if yes put end idx into queue because that end will be new start
        words=set(wordDict)
        n=len(s)
        seen=set()
        queue=deque([0])
        
        while queue:
            start=queue.popleft()
            if start==n:
                return True
            if start in seen:
                continue
            for end in range(start+1,n+1):
                if s[start:end] in words:
                    queue.append(end)
                    if end==n:
                        return True
            seen.add(start)
        
        return False