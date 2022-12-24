class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
#动态规划
#        if n < 2:
#            return n
#        dp = [0] * (n+1)
#        dp[0] = 0
#        dp[1] = 1
#        for i in range(2, n+1):
#            dp[i] = dp[i-1] + dp[i-2]
#        return dp[-1]

#优化
        if n < 2:
            return n
        dp1 = 0
        dp2 = 1
        for _ in range(2, n+1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2