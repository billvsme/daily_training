# coding: utf-8

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.vals = []

    def next(self, val: int) -> float:
        self.vals.append(val)
        self.total += val
        if len(self.vals) > self.size:
            self.total -= self.vals.pop(0)

        return self.total / len(self.vals)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
