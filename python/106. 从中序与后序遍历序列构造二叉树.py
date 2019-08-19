# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-18 13:21:49
"""
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        node = TreeNode(postorder[-1])
        mid = inorder.index(node.val)
        node.left = self.buildTree(inorder[:mid], postorder[:mid])
        node.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return node
