# coding: utf-8
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m-1, n-1
        tail = m + n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                nums1[tail] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[tail] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1

            tail -= 1

        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)
