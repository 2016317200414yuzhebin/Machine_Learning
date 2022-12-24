class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                flag = nums[i] + nums[j] + nums[k]
                if flag == target:
                    return target
                if abs(target - flag) < abs(target - res):
                    res = flag
                if flag > target:
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return res

s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))