class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#双指针
        l = 0
        r = len(height) - 1
        res = 0
        l_max, r_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    res += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    res += r_max - height[r]
                r -= 1
        return res