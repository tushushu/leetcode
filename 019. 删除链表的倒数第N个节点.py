# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-02 10:10:42
"""
from collections import deque


class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        que = deque(maxlen=n + 1)
        node = head
        while node:
            que.append(node)
            node = node.next
        if len(que) == n:
            head = head.next
        else:
            que[0].next = que[1].next
        return head


if __name__ == "__main__":
    pass
