# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-25 18:23:58
"""
from typing import List


class Solution:
    """
    dp[i]表示使用nums[i]的前提下，最长升序子序列是多少
    因此需要遍历i之前的数字，看看哪些元素比i小，dp[j]+1
    表示使用了nums[i]之后，长度要加1，很多博客根本没有
    讲明白怎么回事，让读者误入歧途。
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
