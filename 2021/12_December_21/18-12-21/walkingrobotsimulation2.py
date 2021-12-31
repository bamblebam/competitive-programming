class Robot:
    #store the entire grid in self.grid then just add the steps to global variable and when need to give data return self.steps%len(grid) pos in grid

    def __init__(self, w: int, h: int):
        self.steps=0
        self.grid=[[0, 0, 'South']] + [[i, 0, 'East'] for i in range(1, w)] + \
            [[w - 1, i, 'North'] for i in range(1, h)] + \
            [[i, h - 1, 'West'] for i in range(w - 2, -1, -1)] +\
            [[0, i, 'South'] for i in range(h - 2, 0, -1)]
        
    def step(self, num: int) -> None:
        self.steps+=num
         
    def getPos(self) -> List[int]:
        return self.grid[self.steps%len(self.grid)][:2]

    def getDir(self) -> str:
        return self.grid[self.steps%len(self.grid)][2] if self.steps else "East"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()