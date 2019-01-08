# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-08 10:11:06
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        i = 0
        while 1:
            try:
                if all(map(lambda x: x[i] == strs[0][i], strs)):
                    ret += strs[0][i]
                else:
                    break
            except IndexError:
                break
            i += 1
        return ret


if __name__ == "__main__":
    t = Solution()
    test_cases = [[], ["abc", "", "ab", ""], ["aaa", "aa"]]
    for x in test_cases:
        print(t.longestCommonPrefix(x))
