import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
#分组+哈希
        countAB = collections.Counter(i + j for i in A for j in B)
#        res = 0
#        for i in C:
#            for j in D:
#                if -i-j in countAB:
#                    res += countAB[-i-j]
#        return res

        return sum(countAB.get(-i-j, 0) for i in C for j in D)