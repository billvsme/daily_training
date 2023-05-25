# coding: utf-8
from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hash_map = defaultdict(lambda :0)
        for c in s:
            hash_map[c] += 1

        ans = 0
        for v in hash_map.values():
            if v % 2 == 1:
                ans += 1

        return ans <= 1

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_set = set()
        for c in s:
            if c in s_set:
                s_set.remove(c)
            else:
                s_set.add(c)

        return len(s_set) <= 1


print(Solution().canPermutePalindrome("code"))
print(Solution().canPermutePalindrome("aab"))
