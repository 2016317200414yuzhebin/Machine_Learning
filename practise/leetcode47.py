class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        def backtrack(nums):
            if not nums:
                if temp in res:
                    return 
                else:
                    res.append(temp[:])
                    return
            for num in nums:
                temp.append(num)
                nums_temp = nums[:]
                nums_temp.remove(num)
                backtrack(nums_temp)
                temp.pop()
        backtrack(nums)
        return res