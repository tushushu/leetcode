# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-10 10:43:00
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack1 = []
        stack2 = [-1]
        for i, c in enumerate(s):
            if stack1 and stack1[-1] == "(" and c == ")":
                stack1.pop()
                stack2.pop()
            else:
                stack1.append(c)
                stack2.append(i)
        ret = 0
        stack2.append(len(s))
        for i in range(len(stack2) - 1):
            ret = max(ret, stack2[i + 1] - stack2[i] - 1)
        return ret


if __name__ == "__main__":
    t = Solution()
    print(t.longestValidParentheses(")"))
