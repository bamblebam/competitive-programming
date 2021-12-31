class Solution:
    def nthMagicalNumber(self, N, A, B):
        #use binary search
        #the nums below x that are divisible by a are x/a
        #check if the magic nums below mid are less than n if yes update l else r
        lcm, Q = A*B//gcd(A,B), 10**9 + 7
        
        beg, end = 0, N * min(A,B)
        while beg < end:
            mid = (beg + end)//2
            if mid//A + mid//B - mid//lcm < N:
                beg = mid + 1
            else:
                end = mid
        
        return beg % Q