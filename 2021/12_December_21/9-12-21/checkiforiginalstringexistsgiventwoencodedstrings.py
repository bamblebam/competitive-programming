class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        #go through both the strings and check the difference
        #this is bruteforce
        
        n1=len(s1)
        n2=len(s2)
        
        def getLength(s):
            ans={int(s)}
            for i in range(1,len(s)):
                ans|={x+y for x in getLength(s[:i]) for y in getLength(s[i:])}
            return ans
        
        @cache
        def helper(i,j,diff):
            if i==len(s1) and j==len(s2):
                return diff==0
            if i<len(s1) and s1[i].isdigit():
                ii=i
                while ii<n1 and s1[ii].isdigit():
                    ii+=1
                for x in getLength(s1[i:ii]):
                    if helper(ii,j,diff-x):
                        return True
            elif j<len(s2) and s2[j].isdigit():
                jj=j
                while jj<n2 and s2[jj].isdigit():
                    jj+=1
                for x in getLength(s2[j:jj]):
                    if helper(i,jj,diff+x):
                        return True
            elif diff==0:
                if i<n1 and j<n2 and s1[i]==s2[j]:
                    return helper(i+1,j+1,0)
            elif diff>0:
                if i<n1:
                    return helper(i+1,j,diff-1)
            else:
                if j<n2:
                    return helper(i,j+1,diff+1)
            return False
        
        return helper(0,0,0)