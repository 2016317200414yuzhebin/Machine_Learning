class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = ''
        if not A:
            return res
        key = set(A[0])
        for i in key:
            minnum = min(a.count(i) for a in A)
            res += minnum * i
        return res