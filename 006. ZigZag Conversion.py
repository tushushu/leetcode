# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-28 10:13:29
"""

from operator import itemgetter


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or s == "":
            return s
        ret = []
        i = j = 0
        down = True
        for c in s:
            ret.append((i, j, c))
            if down:
                if j < numRows - 1:
                    j += 1
                else:
                    down = False
                    j -= 1
                    i += 1
            else:
                if j > 0:
                    j -= 1
                    i += 1
                else:
                    down = True
                    j += 1
        ret.sort(key=itemgetter(1, 0))
        return "".join(map(lambda x: x[2], ret))


if __name__ == "__main__":
    t = Solution()
    s = "LEETCODEISHIRING"
    numRows = 3
    print(t.convert(s, numRows))
