# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-05 10:58:20
@Last Modified by:   tushushu
@Last Modified time: 2018-11-05 10:58:20
"""
from itertools import count


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = count(1)
        node = head
        num = 0
        while node:
            num = next(nums)
            node = node.next

        k = num // 2
        node = head
        for _ in range(k):
            node = node.next
        return node
