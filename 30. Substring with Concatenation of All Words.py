<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:41:32 2018

@author: Administrator
"""


class Solution:
    def findSubstring(self, s, words):
        res = []
        stack = []
        l = len(words[0])
        m = len(words)
        n = len(s)
        for i in range(l):
            j = i
            while j+l <= n:
                word = s[j:j+l]
                try:
                    k = words.index(word)
                    stack.append(words.pop(k))
                except:
                    if word not in stack:
                        while stack:
                            words.append(stack.pop())
                    else:
                        stack.append(word)
                        tmp = None
                        while 1:
                            tmp = stack.pop(0)
                            if tmp == word:
                                break
                            else:
                                words.append(tmp)
                if len(stack) == m:
                    res.append(j+l-m*l)
                    words.append(stack.pop(0))
                j += l
            while stack:
                words.append(stack.pop(0))
        return res

class Solution:
    def find(self, word, words):
        try:
            return words.index(word)
        except:
            return -1
    def findSubstring(self, s, words):
        # 寻找子串
        m = len(words)
        n = len(words[0])
        res = []
        # 建立临时列表存储接收到的字符串
        tmp = ["" for _ in range(n)]
        # 建立words的stack
        words_stacks = [[word for word in words] for _ in range(n)]
        # 建立接收词的stack
        stacks = [[] for _ in range(n)]
        for i, char in enumerate(s):
            for j in range(n):
                # 从不同的起点遍历，起点不满足条件跳出循环
                if i < j:
                    continue
                # 接收字符
                tmp[j] += char
                # 字符串长度满足条件
                if len(tmp[j]) == n:
                    # 从words中查找该字符串
                    idx_w = self.find(tmp[j], words_stacks[j])
                    # words_stack中未找到
                    if idx_w == -1:
                        # 如果在stack中也未找到，则清空对应stack中的元素
                        idx_s = self.find(tmp[j], stacks[j])
                        if idx_s == -1:
                            while stacks[j]:
                                words_stacks[j].append(stacks[j].pop())
                        # 否则把找到的元素及其之前的元素全部pop出去
                        else:                    
                            for _ in range(idx_s):
                                words_stacks[j].append(stacks[j].pop(0))
                            # 交换头尾元素
                            stacks[j].append(stacks[j].pop(0))
                    # words_stack中找到了则把下标加入stack
                    else:
                        stacks[j].append(words_stacks[j].pop(idx_w))
                    # 如果stack的长度满足条件，下标加入结果集
                    if len(stacks[j]) == m:
                        res.append(i - m * n + 1)
                    # 重置tmp中对应的元素
                    tmp[j] = ""
        return res

test = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
test.findSubstring(s, words)

s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
test.findSubstring(s, words)

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
test.findSubstring(s, words)

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
test.findSubstring(s, words)

s = "aaaaaa"
words = ["aaa","aaa"]
test.findSubstring(s, words)

s = "abababab"
words = ["a","b","a"]
test.findSubstring(s, words)
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:41:32 2018

@author: Administrator
"""


class Solution:
    def findSubstring(self, s, words):
        res = []
        stack = []
        l = len(words[0])
        m = len(words)
        n = len(s)
        for i in range(l):
            j = i
            while j+l <= n:
                word = s[j:j+l]
                try:
                    k = words.index(word)
                    stack.append(words.pop(k))
                except:
                    if word not in stack:
                        while stack:
                            words.append(stack.pop())
                    else:
                        stack.append(word)
                        tmp = None
                        while 1:
                            tmp = stack.pop(0)
                            if tmp == word:
                                break
                            else:
                                words.append(tmp)
                if len(stack) == m:
                    res.append(j+l-m*l)
                    words.append(stack.pop(0))
                j += l
            while stack:
                words.append(stack.pop(0))
        return res

test = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
test.findSubstring(s, words)

s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
test.findSubstring(s, words)

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
test.findSubstring(s, words)

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
test.findSubstring(s, words)

s = "aaaaaa"
words = ["aaa","aaa"]
test.findSubstring(s, words)

s = "abababab"
words = ["a","b","a"]
test.findSubstring(s, words)
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
