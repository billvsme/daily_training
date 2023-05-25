# coding: utf-8

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for end in range(n):
            if end+1 >= k and len(set(s[end + 1 - k: end+1])) == k:
                ans += 1
        return ans


print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))
