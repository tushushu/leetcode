# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-15 10:26:11
"""


class Solution:
    def helper(self, s):
        dic = dict()
        i = 0
        for c in s:
            if c in dic:
                yield dic[c]
            else:
                dic[c] = i
                yield i
                i += 1

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pat0 = list(self.helper(pattern))
        ret = []
        for word in words:
            pat = self.helper(word)
            if all(a == b for a, b in zip(pat0, pat)):
                ret.append(word)
        return ret
