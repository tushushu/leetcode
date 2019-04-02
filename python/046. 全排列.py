# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:40:50 2018

@author: Administrator
"""


class Solution:
    def permute(self, nums):
        ret = []
        que = [([x], {x}) for x in nums]
        n = len(nums)
        while que:
            arr, used = que.pop(0)
            if len(arr) is n:
                ret.append(arr)
            else:
                for num in nums:
                    if num not in used:
                        que.append((arr + [num], used | {num}))
        return ret


if __name__ == "__main__":
    t = Solution()
    nums = [1, 2, 3]
    t.permute(nums)
