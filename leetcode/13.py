# coding: utf-8

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        n = len(s)
        for i in range(n-1):
            if hash_map[s[i]] >= hash_map[s[i+1]]:
                res += hash_map[s[i]]
            else:
                res -= hash_map[s[i]]

        return res + hash_map[s[n-1]]


print(Solution().romanToInt("MCMXCIV"))
