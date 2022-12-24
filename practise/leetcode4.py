class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sum = nums1 + nums2
        sum.sort()
        l = len(sum)
        if l % 2 == 0:
            flag = (sum[l/2 - 1] + sum[l/2]) / 2.0
            return float(flag)
        else:
            flag = sum[l/2]
            return float(flag)