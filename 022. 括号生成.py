# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-08 13:44:10
"""


class Solution:
    def generateParenthesis(self, n):
        ret = []
        if n is 0:
            pass
        else:
            m = n * 2
            ret = []
            que = [("", 0)]
            while que:
                parenthesis, n_left = que.pop(0)
                n_right = len(parenthesis) - n_left
                if n_right > n_left or n_left > n:
                    pass
                elif len(parenthesis) == m:
                    ret.append(parenthesis)
                else:
                    que.append((parenthesis + "(", n_left + 1))
                    que.append((parenthesis + ")", n_left))
        return ret
