# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-28 13:56:02
"""
from collections import Counter


class Solution:
    def helper(self, cnt1, cnt2):
        return all(cnt1[k] >= v for k, v in cnt2.items())

    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        ret = []
        cnt2 = Counter()
        for x in B:
            cnt = Counter(x)
            for k, v in cnt.items():
                if cnt2[k] < v:
                    cnt2[k] = v
        for word in A:
            cnt1 = Counter(word)
            if self.helper(cnt1, cnt2):
                ret.append(word)
        return ret


if __name__ == "__main__":
    t = Solution()
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["lo", "eo"]
    print(t.wordSubsets(A, B))
