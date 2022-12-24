class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
#愚蠢一些的贪心
#        if not points or not points[0]:
#            return 0
#        points.sort(key = lambda x: (x[0], x[1]))
#        num = len(points)
#        i = 1
#        flag = points[0]
#        while i < len(points):
#            if flag[1] >= points[i][0]:
#                if points[i][1] <= flag[1]:
#                    flag = points[i]
#                else:
#                    flag = [points[i][0], flag[1]]
#                num -= 1
#            else:
#                flag = points[i]
#            i += 1
#        return num

#聪明一些的贪心
        if not points:
            return 0
        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1
        return ans

s = Solution()
arry = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(s.findMinArrowShots(arry))