# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-22 11:17:25
@Last Modified by:   tushushu
@Last Modified time: 2018-10-22 11:17:25
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1]) if words else 0


def main():
    test = Solution()
    s = "  hello world "
    print(test.lengthOfLastWord(s))


if __name__ == '__main__':
    main()
