from fractions import Fraction

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """
        use fractions library to get rid of floating point errors
        can also keep track of last dx and last dy and take cross product to eliminate floating point issues
        """
        stockPrices.sort()
        ans=0
        prevSlope=None
        for (day1,price1),(day2,price2) in zip(stockPrices,stockPrices[1:]):
            slope=Fraction(price2-price1,day2-day1)
            if prevSlope==None:
                prevSlope=slope
                ans+=1
                continue
            if prevSlope==slope:
                continue
            else:
                prevSlope=slope
                ans+=1
        return ans