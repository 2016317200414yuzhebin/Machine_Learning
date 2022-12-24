class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#笨办法
#        res = []
#        for i in nums1:
#            if i in nums2:
#                if i in res:
#                    pass
#                else:
#                    res.append(i)
#        return res

        return list(set(nums1) & set(nums2))