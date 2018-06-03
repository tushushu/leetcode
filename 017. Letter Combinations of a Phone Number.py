<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:00:39 2018

@author: Administrator
"""
from itertools import product


class Solution:
    def __init__(self):
        self.dic = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}

    def letterCombinations(self, digits):
        if digits:
            combinations = product(*[self.dic[s] for s in digits])
            return [''.join(x) for x in combinations]
        else:
            return []

test = Solution()
test.letterCombinations('23')
test.letterCombinations('')
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:00:39 2018

@author: Administrator
"""
from itertools import product


class Solution:
    def __init__(self):
        self.dic = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}

    def letterCombinations(self, digits):
        if digits:
            combinations = product(*[self.dic[s] for s in digits])
            return [''.join(x) for x in combinations]
        else:
            return []

test = Solution()
test.letterCombinations('23')
test.letterCombinations('')
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
