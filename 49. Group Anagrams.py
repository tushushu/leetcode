# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-11 15:57:43
@Last Modified by:   tushushu
@Last Modified time: 2018-12-11 15:57:43
"""
from collections import Counter


class Solution(object):
    def cmp(self, a, b):
        if len(a) != len(b):
            return False
        else:
            return all(v == b[k] for k, v in a.items())

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        patterns = []
        ret = []
        for s in strs:
            p = Counter(s)
            flag = 0
            for i, pattern in enumerate(patterns):
                if self.cmp(p, pattern):
                    ret[i].append(s)
                    flag = 1
                    break
            if flag == 0:
                patterns.append(p)
                ret.append([s])
        return ret


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    t = Solution()
    print(t.groupAnagrams(strs))
