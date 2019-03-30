# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-30 21:47:21
"""


class Solution:
    def jump(self, nums: int) -> int:
        n = len(nums)
        if n is 0:
            return 0
        i = 0
        cnt = 0
        while i != n - 1:
            i = max(filter(lambda x: x < n, map(
                lambda x: i + x, range(1, nums[i] + 1))),
                key=lambda x: float("inf") if x == n - 1 else x + nums[x])
            cnt += 1
        return cnt


if __name__ == "__main__":
    t = Solution()
    # nums = [2, 3, 1, 1, 4]
    # nums = [1, 2]
    # nums = []
    nums = [3, 2, ]
    print(t.jump(nums))
