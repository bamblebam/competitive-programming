class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
        complex math stuff
        _9 _9 _9 _9 lets say last num is ____6 and k is 9 then to have 6 as last we need 4 nines
        """
        if num==0:
            return 0
        
        for i in range(1,11):
            if (i*k)%10==num%10 and i*k<=num:
                return i
        return -1
        
        