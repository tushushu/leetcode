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
            if j is -1 or haystack[i] is needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        return i - j if j is m else -1

    def gen_next_arr(self, needle: str)->list:
        """
        假设haystack的下标为i，needle的下标为j
        如果匹配(haystack[i] != needle[j])
        i不动，
        如果j之前的k个字符跟needle的前k个字符相同
        j就可以从k开始，而不是从0开始

        Arguments:
            needle {str} -- 待查找的子串

        Returns:
            list
        """
        # 初始化一个长度与needle的列表，初始值为0
        m = len(needle)
        # next_arr的元素表示子串公共前缀的最大长度
        next_arr = [0 if i else -1 for i, _ in enumerate(range(m))]
        # 初始化，i在列表的第-1位，j在第0位
        i = -1
        j = 0
        while j < m - 1:
            # i和j位置的元素相同
            if i is -1 or needle[i] is needle[j]:
                # 各前进一步
                i += 1
                j += 1
                # 记录当前位置公共前缀的最大值
                next_arr[j] = i
            # i和j位置的元素不同，i后退到上一个不重复的字符
            else:
                i = next_arr[i]
        return next_arr
