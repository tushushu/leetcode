# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:31:08 2018

@author: Administrator
"""


class Solution:
    def strStr(self, haystack, needle):
        try:
            return haystack.index(needle)
        except:
            return -1
