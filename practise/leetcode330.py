import bisect
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """      
#        res = 0
#        l = len(nums)
#        m = n
#        if 1 not in nums:
#            res += 1
#            if n:
#                bisect.insort(nums, 1)
#        if 2 not in nums:
#            res += 1
#            bisect.insort(nums, 2)
#        for i in range(l-1, -1, -1):
#            if i > 0 and nums[i] > nums[i-1] * 2:
#                res += 1
#                bisect.insort(nums, nums[i]//2)
#        if sum(nums) < n:
#            num = nums[-1]
#            while num < (m+1) // 2:
#                res += 1
#                m = (m+1) // 2
#                bisect.insort(nums, m)
#            if sum(nums) < n:
#                res += 1
#        return nums, res

        res, x = 0, 1
        length, index = len(nums), 0
        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                res += 1
        return res 
s = Solution()
print(s.minPatches([], 16))