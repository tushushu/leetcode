# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-22 13:59:15
"""


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        j = 1
        for i in range(n):
            c = chars.pop(0)
            if i == 0:
                chars.append(c)
            else:
                if c == chars[-1]:
                    j += 1
                else:
                    if j > 1:
                        chars.extend(list(str(j)))
                    else:
                        pass
                    chars.append(c)
                    j = 1
        if j > 1:
            chars.extend(list(str(j)))
        print(chars)


if __name__ == "__main__":
    chars = []
    t = Solution()
    t.compress(chars)
