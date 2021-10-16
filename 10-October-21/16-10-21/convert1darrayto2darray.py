class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k=len(original)
        if k!=m*n:
            return list()
        ans=list()
        cutoff=k//m
        for i in range(m):
            temp=list()
            for j in range(cutoff):
                temp.append(original.pop(0))
            ans.append(temp)
        return ans