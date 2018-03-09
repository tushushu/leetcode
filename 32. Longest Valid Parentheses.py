# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:40:41 2018

@author: Administrator
"""


class Solution:
    def longestValidParentheses(self, s):
        # get indexes of inValid parentheses
        stack = [-1]
        # record how many '(' we have
        cnt = 0
        for i, char in enumerate(s):
            if char is '(':
                stack.append(i)
                cnt += 1
            else:
                if stack and cnt > 0:
                    stack.pop()
                    cnt -= 1
                else:
                    stack.append(i)
        # in case the stack left one or zero elements
        stack.append(len(s))
        # get the length of the longestValidParentheses
        res = 0
        for i in range(0, len(stack) - 1):
            res = max(res, stack[i+1] - stack[i] - 1)
        return res
