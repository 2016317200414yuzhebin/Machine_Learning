class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#回溯算法
        ans = []
        l = []
        def backtrack(nums):
            if not nums:
                # 注意浅拷贝
                ans.append(l[:])
                return
            for num in nums:
                # 1.设置现场
                l.append(num) 
                # 注意浅拷贝
                nums_temp = nums[:]
                nums_temp.remove(num)
                # 2.递归
                backtrack(nums_temp)
                # 3.恢复现场
                l.pop()
        backtrack(nums)
        return ans