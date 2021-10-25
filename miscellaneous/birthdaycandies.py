import heapq
from collections import Counter
def birthdaycandies(m,n,arr):
    candies=[[0,0] for _ in range(n)]
    arr_sum=sum(arr)
    uniques=0
    keys,values=range(1,m+1),arr
    t=0
    l=len(keys)
    while arr_sum>0 and uniques!=m:
        print(arr_sum,uniques)
        for i in range(n):
            num,type_=candies[i][0],candies[i][1]
            while values[t]==0 and sum(values)>0:
                t+=1
                t%=l
            if type_==0:
                candies[i][0],candies[i][1]=num+1,keys[t]
                values[t]-=1
                t+=1
                t%=l
                uniques+=1
            if num!=0:
                if values[type_-1]>0:
                    candies[i][0]+=1
                    values[type_-1]-=1
                    arr_sum-=1
    print(candies)
    
if __name__=='__main__':
    n=6
    m=2
    arr=[8,4]
    birthdaycandies(m,n,arr)
                
        