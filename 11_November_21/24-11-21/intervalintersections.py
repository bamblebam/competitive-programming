class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=list()
        i=j=0
        while i<len(firstList) and j<len(secondList):
            l=max(firstList[i][0],secondList[j][0])
            r=min(firstList[i][1],secondList[j][1])
            if l<=r:
                ans.append([l,r])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
        return ans
                