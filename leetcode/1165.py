# coding: utf-8

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_map = {k: i for i, k in enumerate(keyboard)}
        location = 0
        ans = 0
        for w in word:
            ans += abs(location - keyboard_map[w])
            location = keyboard_map[w]

        return ans


keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"

print(Solution().calculateTime(keyboard, word))
