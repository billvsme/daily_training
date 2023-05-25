# coding: utf-8

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len, hash_map = 0, defaultdict(lambda :0)

        start = 0
        for end in range(len(s)):
            hash_map[s[end]] += 1

            if len(hash_map) <= 2:
                max_len = max(max_len, end - start + 1)
            else:
                while len(hash_map) > 2:
                    hash_map[s[start]] -= 1
                    if hash_map[s[start]] == 0:
                        del hash_map[s[start]]
                    start += 1

        return max_len


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
