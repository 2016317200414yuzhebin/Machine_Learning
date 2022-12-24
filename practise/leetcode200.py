class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.nums_of_grid = 0
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.nums_of_grid += 1
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root:
            father = self.father[x]
            self.father[x] = root
            x = father
        return root
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
        self.nums_of_grid -= 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        uf = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                uf.add((i, j))
                if j > 0 and grid[i][j-1] == "1":
                    uf.merge((i, j), (i, j-1))
                if i > 0 and grid[i-1][j] == "1" and not uf.isConnected((i, j), (i-1, j)):
                    uf.merge((i, j), (i-1, j))   
        return uf.nums_of_grid

s = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(s.numIslands(grid))