class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        '''
        use counter to store the number of times a bag with a particular number of beans appears
        sort it on the basis of size of bag
        go over the counter and at each turn the total number of beans removed will be the lenght of non zero bags*num we are trying to get all other nums to
        subtract that from total number of beans
        that is ans for that turn
        then just decrement the length to remove those bags since we won't consider them for next turn
        '''
        count=Counter(beans)
        count=list(sorted(count.items(),key=lambda x:(x[0],x[1])))
        
        n=len(count)
        m=len(beans)
        total=sum(beans)
        ans=total
        
        for i in range(n):
            num,val=count[i]
            x=total-m*num
            ans=min(ans,x)
            m-=val
        
        return ans
            
            
            