<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:01:48 2018

@author: Administrator
"""


class Solution:
    def helper(self, s):
        cmp = ''
        res = []
        for char in s:
            if char == cmp:
                res[-2] += 1
            else:
                res.extend([1, char])
                cmp = char
        return ''.join(map(str, res))

    def countAndSay(self, n):
        res = '1'
        for _ in range(n-1):
            res = self.helper(res)
        return res
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:01:48 2018

@author: Administrator
"""

class Solution:
    def helper(self, s):
        cmp = s[0]
        cnt = 0
        res = ''
        for char in s:
            if s == cmp:
                cnt += 1
            else:
                res += str(cnt)
                cmp = s
                cnt = 0
        res += str(cnt)
        return res
        
        
    def countAndSay(self, n):
        res = str(n)
        for _ in range(n):
            res = self.helper(res)
        return res

>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
