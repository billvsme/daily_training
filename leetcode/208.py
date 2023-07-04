# coding: utf-8
import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children[c]
        current.isword = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            current = current.children.get(c)
            if current is None:
                return False

        return current.isword

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return False
        return True
