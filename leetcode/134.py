# coding: utf-8
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        total = 0
        start = 0
        for i in range(len(cost)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        if total < 0:
            return -1

        return start


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))
