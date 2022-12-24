# -*- coding: utf-8 -*-
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#两次循环
#        for i, value1 in enumerate(nums):
#            for j, value2 in enumerate(nums[i+1:]):
#                if target == value1 + value2:
#                    return [i, i+j+1]

#散列表
#        map ={}
#        for i, value in enumerate(nums):
#            if target-value in map:
#                return [map[target-value], i] #散列表时间复杂度是O(1)
#            else:
#                map[value] = i

#头尾指针
        i = 0
        j = len(nums) - 1
        nums.sort()
        while(i < j):
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else :
                return [i, j]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))