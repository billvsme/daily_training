# coding: utf-8

class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set([n])
        while n != 1:
            n = sum(int(c) ** 2 for c in str(n))
            if n in n_set:
                return False
            else:
                n_set.add(n)

        return True


print(Solution().isHappy(19))
