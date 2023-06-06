# coding: utf-8
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        i = 0
        while i < min_len:
            if any(s[i] != strs[0][i] for s in strs):
                break
            i += 1

        return strs[0][:i]


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
