# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-21 10:22:35
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        end = None
        ret = 0
        for i in range(n - 1, -1, -1):
            if s[i] is " ":
                if end is None:
                    pass
                else:
                    return end - i
            else:
                if end is None:
                    end = i
                else:
                    pass
        if end is None:
            pass
        else:
            ret = end + 1
        return ret
