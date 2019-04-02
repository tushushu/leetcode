# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-14 10:35:40
@Last Modified by:   tushushu
@Last Modified time: 2018-11-14 10:35:40
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split()))
