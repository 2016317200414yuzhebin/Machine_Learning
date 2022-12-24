class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
#直接排序
        return sorted([(i, j) for i in range(R) for j in range(C)], key = lambda x: (abs(x[0]-r0) + abs(x[1]-c0)))