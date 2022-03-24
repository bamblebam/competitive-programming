class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """
        pattern[0] will always be at the first pos and pattern[1] will always be at the last pos 
        use them to calculate the number of subsequences
        """
        nt=list()
        for x in text:
            if x in pattern:
                nt.append(x)
        nt="".join(nt)
        
        def helper(s):
            total=0
            seen=0
            for x in s:
                if x==pattern[1]:
                    total+=seen
                if x==pattern[0]:
                    seen+=1
            return total
        
        return max(helper(nt+pattern[1]),helper(pattern[0]+nt))
        