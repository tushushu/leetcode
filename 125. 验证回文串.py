# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-16 12:01:12
"""
from itertools import chain

CHAR = set(map(chr, chain(range(65, 65 + 26),
                          range(97, 97 + 26), range(48, 48 + 10))))


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = 0
        q = len(s) - 1
        while 1:
            while p <= q and s[p] not in CHAR:
                p += 1
            while p <= q and s[q] not in CHAR:
                q -= 1
            if p > q:
                return True
            else:
                if s[p].lower() != s[q].lower():
                    return False
                else:
                    p += 1
                    q -= 1


if __name__ == "__main__":
    t = Solution()
    print(t.isPalindrome("a"))
