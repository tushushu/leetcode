# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-21 14:49:08
"""
from typing import List
from collections import defaultdict

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ret = defaultdict(list)
        que = [(root, 0)]
        while que:
            node, depth = que.pop(0)
            ret[depth].append(node.val)
            depth += 1
            if node.left:
                que.append((node.left, depth))
            if node.right:
                que.append((node.right, depth))
        return [ret[i] for i in range(len(ret))]
