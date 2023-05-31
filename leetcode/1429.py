# coding: utf-8
from typing import List
from collections import deque, Counter


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hash_map = Counter(nums)
        self.values = deque(nums)

    def showFirstUnique(self) -> int:
        while self.values and self.hash_map[self.values[0]] > 1:
            self.values.popleft()

        return self.values[0] if self.values else -1

    def add(self, value: int) -> None:
        self.hash_map[value] += 1
        self.values.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
