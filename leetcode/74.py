# coding: utf-8
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n*m-1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//m][mid % m] == target:
                return True
            elif matrix[mid//m][mid % m] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(Solution().searchMatrix(matrix, target))
