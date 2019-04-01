# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-27 11:23:16
"""


class Solution:
    def permuteUnique(self, nums):
        ret = []
        unique = set()
        que = []
        for i, num in enumerate(nums):
            if num not in unique:
                que.append(([num], {i}))
                unique.add(num)
        n = len(nums)
        while que:
            arr, used = que.pop(0)
            if len(arr) is n:
                ret.append(arr)
            else:
                unique = set()
                for i, num in enumerate(nums):
                    if i not in used and num not in unique:
                        que.append((arr + [num], used | {i}))
                        unique.add(num)
        return ret


if __name__ == "__main__":
    t = Solution()
    nums = []
    print(t.permuteUnique(nums))
