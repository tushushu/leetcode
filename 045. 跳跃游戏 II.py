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
            # print("start", i, cnt)
            i = max(filter(lambda x: x < n, map(
                    lambda x: i + x, range(1, nums[i] + 1))),
                    key=lambda x: x + nums[x])
            cnt += 1
            # print("end", i, cnt)
        return cnt


if __name__ == "__main__":
    t = Solution()
    # nums = [2, 3, 1, 1, 4]
    nums = [1, 2]
    # nums = []
    print(t.jump(nums))
