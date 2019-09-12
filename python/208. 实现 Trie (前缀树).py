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
        self.tree = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word == "":
            return
        tree = self.tree
        for c in word:
            if not c in tree:
                tree[c] = dict()
            tree = tree[c]
        tree[None] = dict()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        return True if None in tree else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.tree
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True
