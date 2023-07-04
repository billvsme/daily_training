# coding: utf-8
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(int)

        set1 = set()

        for i, (x, y) in enumerate(equations):
            graph[(x, y)] = values[i]
            graph[(y, x)] = 1/values[i]
            set1 |= {x, y}

        for k in set1:
            for i in set1:
                for j in set1:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]

        rest = []

        for x, y in queries:
            if graph[(x, y)]:
                rest.append(graph[(x, y)])
            else:
                rest.append(-1)

        return rest


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(Solution().calcEquation(equations, values, queries))
