class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num = 0
        connection = 0
        for i, value1 in enumerate(grid):
            for j, value2 in enumerate(value1):
                if value2:
                    if i > 0 and grid[i-1][j]:
                        connection += 1
                    if j > 0 and value1[j-1]:
                        connection += 1
                    num += 1
        return 4 * num - 2 * connection