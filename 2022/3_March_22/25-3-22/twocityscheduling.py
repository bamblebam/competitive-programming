class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        send all the passengers to first city
        then get the diff between prices of city2 and city1
        then send the n smallest diff people to city 2
        
        We put all of them to 1 city and pay 10 + 30 + 400 + 30
        Now, evaluate differences: 10, 170, -350, -10.
        Choose 2 smallest differences, in this case it is -350 and -10 (they are negative, so we can say we get a refund)
        Evaluate final sum as 10 + 30 + 400 + 30 + -350 + -10 = 110
        
        think of this as getting a refund from the n people going to city 2
        """
        first=[i for i,j in costs]
        diff=[j-i for i,j in costs]
        return sum(first)+sum(sorted(diff)[:len(costs)//2])