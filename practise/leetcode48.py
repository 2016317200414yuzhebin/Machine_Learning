class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
#        n = len(matrix)
#        m = [[0] * n for _ in range(n)]
#        for i in range(n):
#            for j in range(n):
#                m[j][n-i-1] = matrix[i][j]
#        matrix[:] = m #浅拷贝

        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                #四个一组
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]