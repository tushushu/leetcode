"""
@Author: tushushu
@Date: 2018-12-20 15:07:02
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_number(self, l):
        # 将各位数字相加
        head = l
        ret = n = 0
        while head:
            ret += head.val * 10 ** n
            head = head.next
            n += 1
        return ret

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 求和
        num = self.get_number(l1) + self.get_number(l2)
        # 结果生成链表
        ret = ListNode(None)
        head = ret
        while 1:
            num, k = divmod(num, 10)
            head.next = ListNode(k)
            head = head.next
            if num == 0:
                break
        return ret.next
