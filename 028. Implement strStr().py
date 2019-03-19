# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:31:08 2018

@author: Administrator
"""


class Solution:
    def strStr(self, haystack: str, needle: str)->int:
        """查找子串在被查找的字符串中出现的下标，查不到返回-1

        Arguments:
            haystack {str} -- 被查找的字符串
            needle {str} -- 待查找的子串

        Returns:
            int
        """

        next_arr = self.gen_next_arr(needle)
        n = len(haystack)
        m = len(needle)
        i = j = 0
        while i < n and j < m:
            if haystack[i] is needle[j]:
                i += 1
                j += 1
            elif j is not 0:
                j = next_arr[j - 1]
            else:
                i += 1
        return i - j if j is m else -1

    def gen_next_arr(self, needle: str)->list:
        """用临时数组存储匹配失败后，下一次匹配时needle的下标

        Arguments:
            needle {str} -- 待查找的子串

        Returns:
            list
        """

        i = 0
        m = len(needle)
        next_arr = [0 for _ in range(m)]
        j = 1
        while j < m:
            if needle[j] is needle[i]:
                next_arr[j] = i + 1
                i += 1
                j += 1
            elif i is not 0:
                i = next_arr[i - 1]
            else:
                next_arr[j] = 0
                j += 1
        return next_arr
