# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-27 10:56:40
@Last Modified by:   tushushu
@Last Modified time: 2018-10-27 10:56:40
"""
from itertools import product


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(j == s for j, s in product(J, S))
