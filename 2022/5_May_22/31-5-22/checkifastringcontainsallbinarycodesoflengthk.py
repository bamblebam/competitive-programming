class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        generate all substrings of size k and check if the number of substrings is 2**k or not
        """
        subs=set()
        n=len(s)
        for i in range(n-k):
            subs.add(s[i:i+k])
        if len(subs)==2**k:
            return True
        return False