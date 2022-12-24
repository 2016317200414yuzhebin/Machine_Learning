import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#双指针
#        i = 0
#        j = len(nums) - 1
#        while i <= j:
#            if nums[i] != target and nums[j] != target:
#                i += 1
#                j -= 1
#            elif nums[i] == target and nums[j] != target:
#                j -= 1
#            elif nums[i] != target and nums[j] == target:
#                i += 1
#            else:
#                break
#        return [i, j] if i <= j else [-1, -1]

#二分查找
        l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        return [l, r-1] if l < r else [-1, -1]