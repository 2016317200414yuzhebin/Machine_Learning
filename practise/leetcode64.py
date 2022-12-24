class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
#动态规划
#        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
#        dp[0][0] = grid[0][0]
#        for i in range(1, len(grid)):
#            dp[i][0] = dp[i-1][0] + grid[i][0]
#        for j in range(1, len(grid[0])):
#            dp[0][j] = dp[0][j-1] + grid[0][j]
#        for i in range(1, len(grid)):
#            for j in range(1,len(grid[0])):
#                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#        return dp[len(grid)-1][len(grid[0])-1]

#改进空间复杂度
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]