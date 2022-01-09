class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #the robot loops through the instructions
        #if after one set of instructions it is back at its og position or not facing the same way it can complete the loop in either 1 or 3 turns
        #can also be checked by going through the sequence 4 times, if at og position it is ok
        x,y,dx,dy=0,0,0,1
        for l in instructions:
            if l=="G":
                x,y=x+dx,y+dy
            elif l=="L":
                dx,dy=-dy,dx
            else:
                dx,dy=dy,-dx
        return (x,y)==(0,0) or (dx,dy)!=(0,1)