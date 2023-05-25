# coding: utf-8
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        return all(
            a == b or ([a, b] in similarPairs) or ([b, a] in similarPairs)
            for a, b in zip(sentence1, sentence2)
        )


sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]

print(Solution().areSentencesSimilar(sentence1, sentence2, similarPairs))
