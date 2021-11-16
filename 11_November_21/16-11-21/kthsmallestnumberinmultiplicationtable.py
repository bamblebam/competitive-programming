class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(x):
            #binary search to check if x is the kth smallest number
            count=0
            for i in range(1,m+1):
                count+=min(x//i,n) #in a row the biggest element if less than k will be x//i else it will be len of row which is n
            return count>=k
        l,r=1,m*n
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l