# coding: utf-8

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        str_set = set()
        n = len(s)
        res = 0

        while end < n:
            while s[end] in str_set:
                str_set.remove(s[start])
                start += 1

            str_set.add(s[end])
            res = max(res, len(str_set))

            end += 1

        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))
