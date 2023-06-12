# coding: utf-8
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = Counter(s)
        hash_map_t = Counter(t)

        return hash_map_s == hash_map_t


s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))
