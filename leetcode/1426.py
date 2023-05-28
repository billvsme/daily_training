# coding: utf-8
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0
        for a in arr:
            if a+1 in arr_set:
                ans += 1

        return ans


print(Solution().countElements([1, 2, 3]))
