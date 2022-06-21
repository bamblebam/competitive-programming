class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans=0
        prev=0
        for bound,percentage in brackets:
            if prev>income:
                break
            taxableIncome=min(bound,income)-prev
            prev=bound
            ans+=taxableIncome*percentage/100
        return ans