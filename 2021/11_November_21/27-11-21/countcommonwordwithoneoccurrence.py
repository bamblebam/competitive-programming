class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1=Counter(words1)
        words2=Counter(words2)
        count=0
        for k,v in words1.items():
            if words1[k]==1 and words2[k]==1:
                count+=1
        return count
                