class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None:
            return A
        m, n = len(A), len(A[0])
        for i in range(m):
            A[i].reverse()
            for j in range(n):
                A[i][j] = -A[i][j] + 1
        return A
