<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:11:16 2018

@author: Administrator
"""


class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        left = set(['(', '[', '{'])
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if stack and dic[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:11:16 2018

@author: Administrator
"""


class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        left = set(['(', '[', '{'])
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if stack and dic[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
