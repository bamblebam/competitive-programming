class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack=list()
        for word in words:
            x=[0]*26
            for c in word:
                x[ord(c)-ord('a')]+=1
            key="".join(list(map(str,x)))
            if stack and stack[-1][0]==key:
                continue
            stack.append((key,word))
        return [x[1] for x in stack]