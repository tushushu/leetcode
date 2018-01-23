# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:05:28 2018

@author: Administrator
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ""
        for i, char in enumerate(s):
            tmp1 = tmp2 = ""
            #odd
            left = right = i
            while 1:
                if left is -1 or right == n or s[left] is not s[right]:
                    tmp1 = s[left+1:right]
                    break
                else:
                    left -= 1
                    right += 1
            #even
            left = i
            right = i + 1
            while 1:
                if left is -1 or right == n or s[left] is not s[right]:
                    tmp2 = s[left+1:right]
                    break   
                else:
                    left -= 1
                    right += 1
            #compare odd and even str
            if len(tmp2) > len(tmp1):
                tmp = tmp2
            else:
                tmp = tmp1
            #compare res and tmp str
            if len(tmp) > len(res):
                res = tmp
        return res
