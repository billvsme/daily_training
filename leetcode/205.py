# coding: utf-8

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_a = {}
        hash_map_b = {}
        n = len(s)
        for i in range(n):
            if s[i] not in hash_map_a:
                hash_map_a[s[i]] = t[i]
            else:
                if hash_map_a[s[i]] != t[i]:
                    return False

            if t[i] not in hash_map_b:
                hash_map_b[t[i]] = s[i]
            else:
                if hash_map_b[t[i]] != s[i]:
                    return False

        return True


s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))
