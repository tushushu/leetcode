# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-07-07 20:30:45
@Last Modified by:   tushushu
@Last Modified time: 2021-07-07 20:30:45
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 2:
            return [1, 2, 1]
        result = [1, 2, 1]
        tmp = [1]
        while rowIndex != 2:
            for i in range(0, len(result) - 1):
                tmp.append(result[i] + result[i + 1])
            tmp.append(1)
            result = tmp
            tmp = [1]
            rowIndex -= 1
        return result
