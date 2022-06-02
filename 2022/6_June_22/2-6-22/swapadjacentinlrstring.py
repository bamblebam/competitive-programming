class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/1536718/Python-Check-their-positions-with-Picture-Clean-and-Concise
        
        checking if all R in end have a R in start which is to the left of it
        checking if all L in end have a L in start which is to the right of it
        check if orders of string without X is same
        
        since L can only move to the left so there should be a L to the right of it in start
        similar for R but R can only move to the right so there should be a R to the left of it in start
        """
        n=len(start)
        
        #check if orders of string without X is same
        if start.replace('X',"")!=end.replace('X',""):
            return False
        
        start_indices=defaultdict(list)
        for i,c in enumerate(start):
            if c!="X":
                start_indices[c].append(i)
        
        end_indices=defaultdict(list)
        for i,c in enumerate(end):
            if c!="X":
                end_indices[c].append(i)
        
        #checking if all R in end have a R in start which is to the left of it
        r_start=start_indices['R']
        r_end=end_indices['R']
        if len(r_start)!=len(r_end):
            return False
        for idx in r_end:
            start=r_start.pop(0)
            if start>idx:
                return False
        
        #checking if all L in end have a L in start which is to the right of it
        l_start=start_indices['L']
        l_end=end_indices['L']
        if len(l_start)!=len(l_end):
            return False
        for idx in l_end:
            start=l_start.pop(0)
            if start<idx:
                return False
        
        return True
        
        