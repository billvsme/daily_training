# coding: utf-8
import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children[c]
        current.isword = True

    def match(self, word, index, root):
        if not root:
            return False
        if index == len(word):
            return root.isword
        if word[index] != ".":
            return self.match(word, index+1, root.children.get(word[index]))
        else:
            for c in root.children:
                if self.match(word, index+1, root.children.get(c)):
                    return True

        return False

    def search(self, word: str) -> bool:
        return self.match(word, 0, self.root)
