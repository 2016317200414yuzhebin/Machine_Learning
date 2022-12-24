class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
#动态规划
#        n = len(prices)
#        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
#        for i in range(1, n):
#            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
#            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
#        return dp[-1][0]

#优化
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell