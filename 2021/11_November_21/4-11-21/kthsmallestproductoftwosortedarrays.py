from bisect import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #use binary search to find the k'th element
        #check function returns the total number of cases which are smaller than x
        def check(x):
            total=0
            for n1 in nums1:
                if n1>0:
                    total+=bisect(nums2,x//n1) #n1 is +ve so all elements in nums2 will be increasing so we take all elements that are smaller than x//n1 because that num multiplied by n1 will give us x
                if n1<0:
                    total+=len(nums2)-bisect_left(nums2,math.ceil(x/n1)) #similarly if n1 is -ve nums2 will be decreasing so we take the left part of the array.
                if n1==0 and x>=0:
                    total+=len(nums2) #if n1 is 0 then all nums in nums2 are 0 so only if x is greater than 0 we will add entire nums2
            return total
        #if check returns greater than k that means more than k number of elements are smaller than mid, .ie. it is not the k'th product
        l,r=-10**10-1,10**10+1
        while l+1<r:
            mid=(l+r)//2
            if check(mid)>=k:
                r=mid
            else:
                l=mid
        return l+1
                    