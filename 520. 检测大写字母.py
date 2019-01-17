# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-17 13:21:21
"""
from operator import lt, ge


class Solution:
    def helper(self, it, fn):
        return all(map(lambda x: fn(x, 'a'), it))

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n < 2:
            ret = True
        else:
            it = iter(word)
            a = next(it) < 'a'
            b = next(it) < 'a'
            if a and b:
                ret = self.helper(it, lt)
            elif not(a) and b:
                ret = False
            else:
                ret = self.helper(it, ge)
        return ret


if __name__ == "__main__":
    t = Solution()
    print(t.detectCapitalUse("ggg"))
