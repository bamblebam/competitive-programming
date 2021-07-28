class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        n=len(students)
        q=len(students[0])
        scores=[[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                for k in range(q):
                    scores[i][j]+=int(students[i][k]==mentors[j][k])
                    
        def getscore(index,seen):
            ans=0
            if index==n:
                return 0
            for j in range(n):
                if (seen & (1<<j))==0:
                    ans=max(ans,getscore(index+1,seen | (1<<j)) + scores[index][j])
            return ans
                    
        return getscore(0,0)
                    