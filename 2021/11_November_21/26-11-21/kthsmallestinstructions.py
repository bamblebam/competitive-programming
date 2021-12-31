class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        #use combination to find out whether the sequense is greater or lower than the kth sequence
        #https://leetcode.com/problems/kth-smallest-instructions/discuss/918393/Python-O((m%2Bn)2)-solution-explained
        #comb=nCr
        m,n=destination[0],destination[1]
        ans=""
        for i in range(m+n):
            if k==1:
                ans+='H'*n+'V'*m
                break
            if k<=comb(m+n-1,m):
                n-=1
                ans+="H"
            else:
                ans+='V'
                k-=comb(m+n-1,m)
                m-=1
        return ans