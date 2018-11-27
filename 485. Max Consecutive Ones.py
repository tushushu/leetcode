class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -float('inf')
        tmp = 0
        for num in nums:
            if num:
                tmp += 1
            else:
                ret = max(ret, tmp)
                tmp = 0
        return max(ret, tmp)
