class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        Let's build a list of candidate answers for which the final answer must be one of those candidates. Afterwards, choosing from these candidates is straightforward.

If the final answer has the same number of digits as the input string S, then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome. For example, 23456 had middle part 234, and 233, 234, 235 flipped into a palindrome yields 23332, 23432, 23532. Given that we know the number of digits, the prefix 235 (for example) uniquely determines the corresponding palindrome 23532, so all palindromes with larger prefix like 23732 are strictly farther away from S than 23532 >= S.

If the final answer has a different number of digits, it must be of the form 999....999 or 1000...0001, as any palindrome smaller than 99....99 or bigger than 100....001 will be farther away from S.
        """
        len_n=len(n)
        half_len=(len(n)+1)//2
        candidates=set([str(10**len_n+1),str(10**(len_n-1)-1)])
        prefix=int(n[:half_len])
        for s in map(str,(prefix,prefix-1,prefix+1)):
            if len_n%2:
                candidates.add(s+s[::-1][1:])
            else:
                candidates.add(s+s[::-1])
        candidates.discard(n)
        return min(candidates,key=lambda x: (abs(int(n)-int(x)),int(x)))
        