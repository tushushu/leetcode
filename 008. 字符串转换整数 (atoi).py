# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-04 10:35:43
"""


INT_MAX = 2147483647
INT_MIN = -2147483648

NUMBERS = set("1234567890")
SIGNS = {"+", "-"}


class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        nums = []
        flag = 0
        for c in s:
            if flag == 0:
                if c == " ":
                    pass
                elif c in SIGNS or c in NUMBERS:
                    flag = 1
                    nums.append(c)
                else:
                    return 0
            else:
                if c in NUMBERS:
                    nums.append(c)
                else:
                    break
        if nums:
            if len(nums) == 1 and nums[0] in SIGNS:
                ret = 0
            else:
                ret = int("".join(nums))
        else:
            ret = 0
        return max(INT_MIN, min(INT_MAX, ret))


if __name__ == "__main__":
    test_cases = {
        "": 0,
        "   ": 0,
        "  ab1c ": 0,
        "a": 0,
        "123a": 123,
        "a123": 0,
        " a123": 0,
        " 123a": 123,
        "+123": 123,
        "-123": -123,
        "1": 1,
        "-0": 0,
        "+1": 1,
        "-1": -1,
        " 1": 1,
        " -1": -1,
        " 1 ": 1,
        " -1 ": -1,
        " +123 acb - 234 a": 123,
        "123 ": 123,
        "+123 ": 123,
        "-123 ": -123,
        "2147483999": 2147483647,
        "+2147483999": 2147483647,
        "-2147483999": -2147483648,
        "+": 0,
        "-": 0
    }
    t = Solution()
    for k, v in test_cases.items():
        assert t.myAtoi(k) == v, "%s expected %d but %d" % (k, v, t.myAtoi(k))
    print("Test passed!")
