class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
#愚蠢的方法
#        res = []
#        dis = []
#        for i in points:
#            dis.append(i[0]**2 + i[1]**2)
#        dis.sort()
#        for i in points:
#            d = i[0]**2 + i[1]**2
#            if d in dis[:K]:
#                res.append(i)
#        return res

#理论上应该和上面一样
        return sorted(points, key = lambda x : x[0]**2 + x[1]**2)[:K]