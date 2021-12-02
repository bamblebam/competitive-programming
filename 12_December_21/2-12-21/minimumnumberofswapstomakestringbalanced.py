class Solution:
    def minSwaps(self, s: str) -> int:
        #we remove the balanced brackets, and any open bracket which is left means there is an equal amount of closing brackets
        #that divided by 2 is the number of swaps
        count=0 #the number of open brackets that do not have a corredponding closing bracket. unbalanced open brackets
        for i in s:
            if i=="[":
                count+=1
            elif i=="]" and count>0:
                count-=1
        return (count+1)//2