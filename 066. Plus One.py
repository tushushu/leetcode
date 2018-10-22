class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        p = 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
                continue
            else:
                digits[i] += p
                p = 0
                break
        return [p] + digits if p else digits


def main():
    t = Solution()
    digits = [8, 9, 9, 9]
    print(t.plusOne(digits))


if __name__ == '__main__':
    main()
