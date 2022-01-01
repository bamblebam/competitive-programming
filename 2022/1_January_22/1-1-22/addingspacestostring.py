class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s2=list()
        j=0
        for i in range(len(s)):
            if j<len(spaces) and i==spaces[j]:
                s2.append(" ")
                j+=1
            s2.append(s[i])
        return "".join(s2)