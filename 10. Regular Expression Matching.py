# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:11:05 2018

@author: Administrator
"""
import re


class Solution:
    def isMatch(self, s, p):
        return True if re.compile('^' + p + '$').match(s) else False
