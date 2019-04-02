# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-28 18:35:41
@Last Modified by:   tushushu
@Last Modified time: 2018-10-28 18:35:41
"""


class Solution:
    def toLowerCase(self, s):
        """
        :type str: str
        :rtype: str
        """
        return ''.join(map(chr,
                           map(lambda x: x + 32 if 65 <= x <= 90 else x,
                               map(ord, s))))
