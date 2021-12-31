class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def issub(word1,word2):
            word2=iter(word2)
            return all(char in word2 for char in word1)
        
        strs.sort(key=len,reverse=True)
        
        for i,word in enumerate(strs):
            if all(not issub(word,strs[j]) for j in range(len(strs)) if j!=i):
                return len(word)
            
        return -1