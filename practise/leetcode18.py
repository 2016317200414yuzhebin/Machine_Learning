class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
#双指针
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = len(nums) -1
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    while k < l and nums[k] + nums[l] > target-nums[i]-nums[j]:
                        l -= 1
                    if k == l:
                        break
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
        return res