# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-10 19:20:42
"""
from typings import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        k = len(nums) // 2
        node = TreeNode(nums[k])
        node.left = self.sortedArrayToBST(nums[:k])
        node.right = self.sortedArrayToBST(nums[k+1:])
        return node
