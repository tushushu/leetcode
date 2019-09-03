# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-03 10:06:13
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = []
        ret = []
        n = len(s)
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c != " ":
                tmp.append(c)
            else:
                if tmp:
                    ret.append("".join(tmp))
                    tmp.clear()
        return " ".join(ret)
