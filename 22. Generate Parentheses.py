# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:42:25 2018

@author: Administrator
"""


class Solution:
    def helper(self, m, n, res, left, right):
        result = []
        if right > left or left > n:
            return []
        if m == 0:
            return [res]
        result.extend(self.helper(m-1, n, res+"(", left+1, right))
        result.extend(self.helper(m-1, n, res+")", left, right+1))
        return result

    def generateParenthesis(self, n):
        if n is 0:
            return []
        left = right = 0
        res = ""
        return self.helper(n*2, n, res, left, right)

test = Solution()
test.generateParenthesis(1)
test.generateParenthesis(2)
test.generateParenthesis(3)
test.generateParenthesis(0)
