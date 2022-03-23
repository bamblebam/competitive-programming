class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        sort the array and use 2 pointer approach
        couple the smallest and largest person
        """
        people.sort()
        ans=0
        n=len(people)
        l,r=0,n-1
        while l<=r:
            if people[r]+people[l]>limit:
                ans+=1
                r-=1
            else:
                ans+=1
                r-=1
                l+=1
        return ans