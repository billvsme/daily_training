# coding: utf-8

from typing import List
from collections import defaultdict


class Solution:
    def word_to_number(self, word):
        numbers = []
        for i in range(len(word)-1):
            numbers.append((ord(word[i+1])-ord(word[i])) % 26)

        return ",".join([str(n) for n in numbers])

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        s_map = defaultdict(list)

        for s in strings:
            s_map[self.word_to_number(s)].append(s)

        return list(s_map.values())


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(Solution().groupStrings(strings))
