# coding: utf-8
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map_a = Counter(ransomNote)
        hash_map_b = Counter(magazine)

        for c in hash_map_a:
            if c in hash_map_b and hash_map_b[c] >= hash_map_a[c]:
                pass
            else:
                return False

        return True


print(Solution().canConstruct("aa", "ab"))
