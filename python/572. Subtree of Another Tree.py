# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-06 17:11:14
@Last Modified by:   tushushu
@Last Modified time: 2018-12-06 17:11:14
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, t1, t2):
        que = [[t1, t2]]
        while que:
            a, b = que.pop(0)
            if a.val != b.val:
                return False

            if a.left and b.left:
                que.append([a.left, b.left])
            elif a.left or b.left:
                return False
            else:
                pass

            if a.right and b.right:
                que.append([a.right, b.right])
            elif a.right or b.right:
                return False
            else:
                pass
        return True

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        que = [s]
        while que:
            t1 = que.pop(0)
            if self.isSameTree(t1, t):
                return True
            if t1.left:
                que.append(t1.left)
            if t1.right:
                que.append(t1.right)
        return False
