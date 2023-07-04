# coding: utf-8
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()

        queue.append((beginWord, 1))

        c_set = set()
        wordList = set(wordList)
        for word in wordList:
            for c in word:
                c_set.add(c)

        while queue:
            word, step = queue.popleft()

            for i, c1 in enumerate(word):
                for c2 in c_set:
                    if c1 != c2:
                        word2 = word[:i] + c2 + word[i+1:]
                        if word2 in wordList:
                            if word2 == endWord:
                                return step + 1
                            queue.append((word2, step+1))
                            wordList.remove(word2)

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
