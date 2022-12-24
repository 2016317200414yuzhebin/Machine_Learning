class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        map1 = [[value, i] for i, value in enumerate(nums1)]
        map2 = [[value, i] for i, value in enumerate(nums2)]
        map1.sort(key = lambda x: (-x[0]))
        map2.sort(key = lambda x: (-x[0]))
        res = []
        i, j = 0, 0
        while len(res) < k:
            if i < len(nums1) and map1[i][0] >= map2[j][0]:
                if i == 0:
                    res.append(map1[i][0])
                if i > 0 and map1[i][1] > map1[i-1][1]:
                    res.append(map1[i][0])
                i += 1
            else:
                if j == 0:
                    res.append(map2[j][0])
                if j > 0 and map2[j][1] > map2[j-1][1]:
                    res.append(map2[j][0])
                j += 1
        return map1,  map2

s = Solution()
nums1 = [6, 7]
nums2 = [6, 0, 4]
print(s.maxNumber(nums1, nums2, 5))