class Solution:
    def appealSum(self, s: str) -> int:
        
        """
        use a dict to keep track of the last indice where the letter was seen
        calculate contribution for each char in s
        if a letter is not seen it will add + 1 to all the prev strings else only consider strings between char and its last occurence
        calculate total arrs by left*right where left is all pos left of the letter and right is to the right of the letter
        
        for abbca
        
        b
        left
        _
        a
        right
        _
        b
        bc
        bca
        so left =2 right =4
        
        for second b
        left
         _
         b X
        ab X
        right
        _
        c
        ca
        
        dont consider the ones with X because they already have the prev b so left =1 right=3
        """
        ans=0
        seen=dict()
        n=len(s)
        
        for i,c in enumerate(s):
            if c in seen:
                left=i-seen[c]
                right=n-i
                ans+=left*right
            else:
                left=i+1
                right=n-i
                ans+=left*right
            seen[c]=i
        return ans