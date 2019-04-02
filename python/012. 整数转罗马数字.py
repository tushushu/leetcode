# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-05 17:35:43
"""

NUMS = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "M", "MM", "MMM"]]


class Solution:
    def intToRoman(self, num):
        ret = ["", "", "", ""]
        n = len(ret) - 1
        i = 0
        while num:
            num, x = divmod(num, 10)
            ret[n - i] = NUMS[i][x]
            i += 1
        return "".join(ret)
