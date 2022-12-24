class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = sorted(nums)
        map = {}
        for i, value in enumerate(a):
            if i > 0 and value == a[i-1]:
                continue
            else:
                map[value] = i
        return [map[n] for n in nums]

#计数
#        dic = [0]*101
#        for n in nums:
#            dic[n] += 1
#        return [sum(dic[0:n]) for n in nums]