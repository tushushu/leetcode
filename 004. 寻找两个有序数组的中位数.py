"""
@Author: tushushu
@Date: 2018-12-26 10:17:06
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        tot = (m + n) // 2 - 2
        low = -1
        high = m
        while 1:
            i = (low + high) // 2
            j = tot - i
            cond1 = (i == -1 or j == n - 1 or nums1[i] <= nums2[j + 1])
            cond2 = (j == -1 or i == m - 1 or nums2[j] <= nums1[i + 1])
            if cond1 and cond2:
                if (m + n) % 2:
                    if j == n - 1:
                        ret = nums1[i + 1]
                    elif i == m - 1:
                        ret = nums2[j + 1]
                    else:
                        ret = min(nums1[i + 1], nums2[j + 1])
                else:
                    if j == -1:
                        left = nums1[i]
                    elif i == -1:
                        left = nums2[j]
                    else:
                        left = max(nums1[i], nums2[j])
                    if j == n - 1:
                        right = nums1[i + 1]
                    elif i == m - 1:
                        right = nums2[j + 1]
                    else:
                        right = min(nums1[i + 1], nums2[j + 1])
                    ret = (left + right) / 2
                return ret
            elif cond1:
                low = i + 1
            else:
                high = i - 1


if __name__ == "__main__":
    t = Solution()
    nums1 = [1, 2, 3, 6]
    nums2 = [4, 5, 8, 9]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2, 3, 6]
    nums2 = [4, 5, 8]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = [1]
    nums2 = [2]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = []
    nums2 = [2]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = []
    nums2 = [2, 4]
    print(t.findMedianSortedArrays(nums1, nums2))
    nums1 = [1]
    nums2 = [1]
    print(t.findMedianSortedArrays(nums1, nums2))
