# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-11 15:57:43
@Last Modified by:   tushushu
@Last Modified time: 2018-12-11 15:57:43
"""
from collections import Counter

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = dict()
        for s in strs:
            cnt = Counter(s)
            pattern = ''.join(c + str(cnt[c]) for c in CHARACTERS if c in cnt)
            # pattern = ''.join(x[0] + str(x[1]) for x in sorted(cnt.items(), key=lambda x:x[0]))
            if pattern in ret:
                ret[pattern].append(s)
            else:
                ret[pattern] = [s]
        return [x for x in ret.values()]


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    t = Solution()
    print(t.groupAnagrams(strs))
