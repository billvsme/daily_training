# coding: utf-8

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        k = 0
        i, j = 0, 0
        find = False
        while j < len(target):
            if source[i] == target[j]:
                find = True
                j += 1
            i += 1

            if i == len(source):
                print(k, i, j)
                if not find:
                    return -1

                k += 1
                i = 0
                find = False

        return k if i == 0 else k + 1


print(Solution().shortestWay("xyz", "xzyxz"))
