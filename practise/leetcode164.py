class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#快排
#        if len(nums) < 2:
#            return 0
#        nums.sort()
#        res = 0
#        for i in range(len(nums)):
#            if i > 0:
#                res = max(res, nums[i]-nums[i-1])
#        return res

#一行
#        return max(y-x for x, y in zip(sorted(nums), sorted(nums)[1:])) if len(nums) >= 2 else 0

#桶排序(桶数为n+1保证间距最大的两个数不会被分到一个桶内)
        if len(nums) < 2:
            return 0
        min_val, max_val, n = float('inf'), float('-inf'), len(nums)
        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        if min_val == max_val:
            return 0
        mins = [0] * (n + 1)
        maxs = [0] * (n + 1)
        has_num = [False] * (n + 1)
        for num in nums:
            index = int((num - min_val) * n / (max_val - min_val))
            mins[index] = num if not has_num[index] else min(mins[index], num)
            maxs[index] = num if not has_num[index] else max(maxs[index], num)
            has_num[index] = True
        max_len = 0
        m = maxs[0]
        for i in range(1, n + 1):
            if has_num[i]:
                max_len = max(max_len, mins[i]-m)
                m = maxs[i]
        return max_len