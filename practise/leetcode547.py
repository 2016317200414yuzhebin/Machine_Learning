class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        country = len(isConnected)
        visited = set()
        res = 0

#深度优先
#        def dfs(self, i):
#            for j in range(country):
#                if isConnected[i][j] == 1 and j not in visited:
#                    visited.add(j)
#                    dfs(j)
#        for i in range(country):
#            if i not in visited:
#                dfs(i)
#                res += 1
#        return res

#广度优先
#        for i in range(country):
#            if i not in visited:
#                queue = []
#                queue.append(i)
#                while queue:
#                    j = queue.pop(0)
#                    visited.add(j)
#                    for k in range(country):
#                        if isConnected[j][k] == 1 and k not in visited:
#                            queue.append(k)
#                res += 1
#        return res

#并查集
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.add(j)
                    uf.merge(i, j)
        return uf.num_of_sets

class UnionFind:
    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0
    
    def find(self, x):
        #路径压缩(递归)
#       
        root = x
        while self.father[root] != None:
            root = self.father[root]
        #路径压缩（迭代）
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1