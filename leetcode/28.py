# coding: utf-8

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i

        return -1


haystack = "sadbutsad"
needle = "sad"

print(Solution().strStr(haystack, needle))
