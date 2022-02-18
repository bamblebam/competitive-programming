class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1>num2:
            num1,num2=num2,num1
        count=0
        if num2==0 or num1==0:
            return count
        while True:
            num2-=num1
            count+=1
            if num1>num2:
                num1,num2=num2,num1
            if num2==0 or num1==0:
                return count
        return count