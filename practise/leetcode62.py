class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
#动态规划
#        if m == 0 or n == 0:
#            return 0
#        dp = [[1] *n for i in range(m)]
#        for i in range(m):
#            dp[i][0] = 1
#        for j in range(n):
#            dp[0][j] = 1
#        for i in range(1, m):
#            for j in range(1, n):
#                dp[i][j] = dp[i-1][j] + dp[i][j-1]
#        return dp[m-1][n-1]

#排列组合
#        import math
#        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

#改进后的动态规划
        if m == 0 or n == 0:
            return 0
        dp = [1] * n
        for i in range(1, m):
            dp[0] = 1
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]