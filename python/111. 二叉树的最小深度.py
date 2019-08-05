# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-05 20:59:48
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        right = self.minDepth(root.right) + 1
        if root.left is None and root.right is not None:
            return right
        left = self.minDepth(root.left) + 1
        if root.right is None and root.left is not None:
            return left
        return min(left, right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    t = Solution()
    print(t.minDepth(root))
