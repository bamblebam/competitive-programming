class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        larry video: https://www.youtube.com/watch?v=K4xFXoqakfA
        sort the people on the basis of height, tallest first and earlier pos early
        then group the people with same height
        and insert different height
        like if all with height 7 are set and we get a height 6 with o tall people it will be at the start of the array
        but if it has 1 taller person it will be to the left of [7,0]
        """
        people.sort(key=lambda x:(-x[0],x[1]))
        ans=list()
        for height,pos in people:
            ans.insert(pos,(height,pos))
        return ans