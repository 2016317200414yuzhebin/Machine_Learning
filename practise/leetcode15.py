class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#        nums.sort()
#        res = []
#        for i, value in enumerate(nums):
#            j = i + 1
#            map = {}
#            while j < len(nums):
#                if -value-nums[j] in map.keys():
#                    flag = [nums[i], nums[map[0-value-nums[j]]], nums[j]]
#                    if flag in res:
#                        pass
#                    else:
#                        res.append(flag)
#                else:
#                    map[nums[j]] = j
#                j += 1
#        return res


        nums.sort()
        res = []
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            k = len(nums) - 1
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[j] + nums[k] > -value:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
        return res

s = Solution()
print(s.threeSum([-2,0,1,1,2]))