class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for sentence in sentences:
            x=len(sentence.split(" "))
            ans=max(ans,x)
        return ans