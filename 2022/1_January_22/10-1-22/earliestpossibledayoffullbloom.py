from functools import cmp_to_key

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        #done using exchange argument algorithm
        #sort the list in such way that they are compare on the basis of total grow time (kinda confusing)
        #then just normally iterate through it and update latest and curr
        #latest is max time or ans, curr is the max plant time
        def compare(a,b):
            p1,g1=a
            p2,g2=b
            return (p1+max(g1,p2+g2))-(p2+max(g2,p1+g1))
        
        times=list(zip(plantTime,growTime))
        times.sort(key=cmp_to_key(compare))
        
        latest,curr=0,0
        for p,g in times:
            latest=max(latest,p+g+curr)
            curr+=p
        
        return latest
        