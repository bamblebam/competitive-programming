class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        create a set of 6 elems
        for each pair of a,b in zip arrays check if one of them exists using &
        if set is empty cannot be created
        else check whether you put the elem in bottom or top row
        """
        s=set(list(range(1,7)))
        n=len(tops)
        for a,b in zip(tops,bottoms):
            s&=set([a,b])
        if not s:
            return -1
        s=list(s)
        flip1=sum(tops[i]==s[0] for i in range(n))
        flip2=sum(bottoms[i]==s[0] for i in range(n))
        return min(n-flip1,n-flip2)