# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-04 14:19:13
"""
from typing import List

mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wyxz"}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ret = [""]
        for d in digits:
            letters = mapping[d]
            n = len(ret)
            for _ in range(n):
                s = ret.pop(0)
                for x in letters:
                    ret.append(s + x)
        return ret
