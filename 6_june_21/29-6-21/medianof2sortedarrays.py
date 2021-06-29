class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        half=(m+n)//2
        l,r=0,m-1
        while True:
            i=(l+r)//2
            j=half-i-2
            left1=nums1[i] if i>=0 else -float('inf')
            left2=nums2[j] if j>=0 else -float('inf')
            right1=nums1[i+1] if (i+1)<m else float('inf')
            right2=nums2[j+1] if (j+1)<n else float('inf')
            if left1<=right2 and left2<=right1:
                if (m+n)%2:
                    return min(right1,right2)
                return (max(left1,left2)+min(right1,right2))/2
            elif left1>right2:
                r=i-1
            else:
                l=i+1