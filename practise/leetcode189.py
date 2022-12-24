class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#最容易想到的
#        for _ in range(k):
#            nums.insert(0, nums.pop())

        nums[:] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))