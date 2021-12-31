# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        r=n
        l=1
        while l<r:
            mid=(l+r)//2
            t=isBadVersion(mid)
            if t:
                r=mid
            else:
                l=mid+1
        return l