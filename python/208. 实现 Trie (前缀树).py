# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-12 14:19:22
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word == "":
            return
        node = self.node
        for c in word:
            if not c in node:
                node[c] = dict()
            node = node[c]
        node[None] = dict()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.node
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return True if None in node else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.node
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
