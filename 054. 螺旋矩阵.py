# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-01 11:47:15
"""
from itertools import cycle


class Solution:
    def spiralOrder(self, matrix):
        ite = cycle(range(4))
        d = next(ite)
        ret = []
        while matrix:
            if d is 0:
                ret.extend(matrix.pop(0))
                d = next(ite)
            elif d is 1:
                if len(matrix[0]) is 1:
                    while matrix:
                        ret.extend(matrix.pop(0))
                else:
                    for row in matrix:
                        ret.append(row.pop())
                d = next(ite)
            elif d is 2:
                ret.extend(matrix.pop()[::-1])
                d = next(ite)
            else:
                if len(matrix[0]) is 1:
                    while matrix:
                        ret.extend(matrix.pop())
                else:
                    for i in range(len(matrix) - 1, -1, -1):
                        ret.append(matrix[i].pop(0))
                d = next(ite)
        return ret


if __name__ == "__main__":
    t = Solution()
    t.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
