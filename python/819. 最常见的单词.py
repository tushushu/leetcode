# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-23 14:42:56
"""

SIGN = set(" !?',;.")


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        paragraph = paragraph.lower()
        cnt = dict()
        start = None
        end = None
        max_cnt = 0
        ret = ""
        for i, c in enumerate(paragraph):
            if c not in SIGN:
                if start is None:
                    start = i
                else:
                    pass
            else:
                if start is None:
                    pass
                else:
                    end = i
                    word = paragraph[start:end]
                    if word in banned:
                        pass
                    else:
                        if word in cnt:
                            cnt[word] += 1
                        else:
                            cnt[word] = 1
                        if cnt[word] > max_cnt:
                            max_cnt = cnt[word]
                            ret = word
                    start = None
                    end = None
        if start is None:
            pass
        else:
            end = i + 1
            word = paragraph[start:end]
            if word in banned:
                pass
            else:
                if word in cnt:
                    cnt[word] += 1
                else:
                    cnt[word] = 1
                if cnt[word] > max_cnt:
                    max_cnt = cnt[word]
                    ret = word
        return ret


if __name__ == "__main__":
    t = Solution()
    t.mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
