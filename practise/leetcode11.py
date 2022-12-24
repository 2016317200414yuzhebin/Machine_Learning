class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#暴力遍历
#        max_area = 0
#        for i, a in enumerate(height):
#            for j, b in enumerate(height):
#                h = min(a, b)
#                area = h * (j-i)
#                max_area = max(max_area, area)
#        return max_area

#双指针
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            area = h * (j-i)
            max_area = max(max_area, area)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max_area