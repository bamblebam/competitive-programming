class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #greedy solution
        #sort both the arrays and just match the corressponding elements
        n=len(seats)
        seats.sort()
        students.sort()
        ans=sum(abs(x-y) for x,y in zip(seats,students))
        return ans