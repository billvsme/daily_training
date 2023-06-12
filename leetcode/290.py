# coding: utf-8


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        p2s = {}
        s2p = {}

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in p2s:
                p2s[pattern[i]] = s[i]
            else:
                if p2s[pattern[i]] != s[i]:
                    return False

            if s[i] not in s2p:
                s2p[s[i]] = pattern[i]
            else:
                if s2p[s[i]] != pattern[i]:
                    return False

        return True


pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))
