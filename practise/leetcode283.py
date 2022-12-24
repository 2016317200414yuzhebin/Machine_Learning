class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#双指针
#        left = right = 0
#        while right < len(nums):
#            if nums[right]:
#                nums[left], nums[right] = nums[right], nums[left]
#                left += 1
#            right += 1

#易想到的方法
#        for i in range(nums.count(0)):
#            nums.remove(0)
#            nums.append(0)

        nums.sort(key=bool, reverse=True)