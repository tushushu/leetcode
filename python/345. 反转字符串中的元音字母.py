# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-09 14:34:02
"""
VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = list(s)
        indexes = []
        vowels = []
        for i, c in enumerate(s):
            if c in VOWELS:
                indexes.append(i)
                vowels.append(c)
        m = len(indexes)
        for i in range(m):
            ret[indexes[i]] = vowels[m - i - 1]
        return "".join(ret)
