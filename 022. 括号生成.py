# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-08 13:44:10
"""


class Solution:
    def generateParenthesis(self, n):
        if n is 0:
            return []
        m = n * 2
        ret = []
        que = [("", 0, 0)]
        while que:
            parenthesis, n_left, n_right = que.pop(0)
            if n_right > n_left or n_left > n:
                pass
            elif len(ret) == m:
                ret.append(parenthesis)
            else:
                que.append((parenthesis + "(", n_left + 1, n_right))
                que.append((parenthesis + ")", n_left, n_right + 1))
