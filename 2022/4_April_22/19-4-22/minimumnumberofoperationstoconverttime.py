class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ans=0
        
        def convert(time):
            h,m=time.split(":")
            return int(h)*60 + int(m)
        
        curr,target=convert(current),convert(correct)
        
        for k in [60,15,5,1]:
            while target-curr>=k:
                target-=k
                ans+=1
        
        return ans