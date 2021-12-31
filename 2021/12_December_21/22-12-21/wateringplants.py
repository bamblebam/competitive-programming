class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        #iterate through plants array, if the capacity is less than required go back, just add steps where required
        n=len(plants)
        steps=0
        t=capacity
        for i,x in enumerate(plants):
            if plants[i]>t:
                t=capacity-plants[i]
                steps+=i*2+1
            else:
                steps+=1
                t-=plants[i]
        return steps