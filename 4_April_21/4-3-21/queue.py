class MyCircularQueue:

    def __init__(self, k: int):
        self.max_len = k
        self.queue = list()

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.max_len:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue) == self.max_len:
            return True
        return False
