# coding: utf-8
from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        paths = []

        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            elif flags[i] == 1:
                return False

            flags[i] = 1

            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False

            flags[i] = -1
            paths.append(i)

            return True

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return []

        return paths[::-1]


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        paths = []

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        paths = []
        while queue:
            pre = queue.popleft()
            paths.append(pre)

            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)

        return paths if numCourses == 0 else []


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(Solution2().findOrder(numCourses, prerequisites))
