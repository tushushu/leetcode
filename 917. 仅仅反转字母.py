# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-03 10:37:14
"""
LETTERS = set([chr(i) for i in range(65, 91)] +
              [chr(i) for i in range(97, 123)])


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if s == "":
            return s
        letters = []
        others = []
        ret = []
        for i, c in enumerate(s):
            if c in LETTERS:
                letters.append(c)
            else:
                others.append((i, c))
        letters.reverse()
        for i in range(len(s)):
            if others and others[0][0] == i:
                _, c = others.pop(0)
                ret.append(c)
            else:
                c = letters.pop(0)
                ret.append(c)
        return "".join(ret)
