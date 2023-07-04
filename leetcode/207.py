# coding: utf-8
from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        ajacency = [[] for _ in range(numCourses)]
        queue = deque()

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            ajacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.popleft()
            numCourses -= 1

            for cur in ajacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)

        return numCourses == 0


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False

            flags[i] = 1

            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False

            flags[i] = -1

            return True

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False

        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]

print(Solution().canFinish(numCourses, prerequisites))
