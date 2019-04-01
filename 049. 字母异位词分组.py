# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-28 16:12:56
"""
from collections import Counter, defaultdict
from itertools import chain

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class Solution(object):
    def get_pattern(self, s):
        cnt = Counter(s)
        ite = ((c, str(cnt[c])) for c in CHARACTERS if c in cnt)
        return ''.join(chain(*ite))

    def groupAnagrams(self, strs):
        patterns = map(lambda x: (self.get_pattern(x), x), strs)
        dic = defaultdict(list)
        for k, v in patterns:
            dic[k].append(v)
        return list(dic.values())
