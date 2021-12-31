import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        angle = random.uniform(0, 2*math.pi)
        inverse_r = self.radius*math.sqrt(random.uniform(0, 1))
        return [inverse_r*math.cos(angle)+self.x_center, inverse_r*math.sin(angle)+self.y_center]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
