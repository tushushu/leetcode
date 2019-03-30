# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-30 21:15:35
"""


class Solution:
    def jump(self, nums: int) -> int:
        n = len(nums)
        i = 0
        cnt = 0
        while i != n - 1:
            print(i, cnt)
            if nums[i] == 1:
                i += 1
            else:
                i = max(filter(lambda x: x < n, map(
                    lambda x: i + x, i + x + nums[i + x],
                    range(1, nums[i] + 1))))
            cnt += 1
            print(i, cnt)
        return cnt + 1


if __name__ == "__main__":
    t = Solution()
    nums = [2, 3, 1, 1, 4]
    print(t.jump(nums))
