# coding: utf-8
import random


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False

        self.hash_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        i = self.hash_map[val]
        self.nums[i] = self.nums[-1]
        self.hash_map[self.nums[-1]] = i
        self.nums.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
