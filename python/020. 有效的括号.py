# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-07 13:26:46
"""

# 左括号集合
LEFT = set(['(', '[', '{'])
# 配对字典
PAIR = {')': '(', ']': '[', '}': '{'}


class Solution:
    def isValid(self, s):
        # 提前终止程序
        if s == "":
            return True
        if len(s) % 2 is 1:
            return False
        if s[-1] in LEFT:
            return False

        # 利用堆栈清空
        stack = []
        for char in s:
            if char in LEFT:
                stack.append(char)
            else:
                if stack and PAIR[char] is stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
