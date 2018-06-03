# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:51:01 2018

@author: Administrator
"""
class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
