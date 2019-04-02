# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-24 21:19:44
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = None
        ret = ""
        for i, c in enumerate(s):
            if c == " ":
                if start is None:
                    ret += c
                else:
                    end = i
                    if start == 0:
                        ret += s[end - 1:: -1]
                    else:
                        ret += s[end - 1: start - 1: -1]
                    ret += c
                    start = None
            else:
                if start is None:
                    start = i
                else:
                    pass
        if start is None:
            pass
        else:
            end = i + 1
            if start == 0:
                ret += s[end - 1:: -1]
            else:
                ret += s[end - 1: start - 1: -1]
        return ret


if __name__ == "__main__":
    t = Solution()
    print(t.reverseWords("Let's take LeetCode contest"))
