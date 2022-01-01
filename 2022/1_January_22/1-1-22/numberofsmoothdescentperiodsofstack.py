class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #go through the array checking if it is smooth descending if yes update temp and add it to ans
        n=len(prices)
        ans=0
        temp=1
        for i in range(n):
            if i==0:
                ans+=temp
                continue
            if prices[i]==prices[i-1]-1:
                temp+=1
                ans+=temp
            else:
                temp=1
                ans+=temp
        return ans