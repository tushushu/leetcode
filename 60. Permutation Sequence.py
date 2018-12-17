# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-17 11:58:33
@Last Modified by:   tushushu
@Last Modified time: 2018-12-17 11:58:33
"""
from itertools import permutations


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        it = permutations(range(1, n + 1), n)
        for _ in range(k - 1):
            next(it)
        return "".join(map(str, next(it)))


if __name__ == "__main__":
    t = Solution()
    print((t.getPermutation(3, 2)))
