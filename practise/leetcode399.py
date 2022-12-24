from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
#图
#        graph = defaultdict(set)
#        weight = defaultdict()
        # 建图
#        for idx, equ in enumerate(equations):
#            graph[equ[0]].add(equ[1])
#            graph[equ[1]].add(equ[0])
#            weight[tuple(equ)] = values[idx]
#            weight[(equ[1], equ[0])] = float(1 / values[idx])

        # 深度遍历(DFS)
#        def dfs(start, end, vistied):
            # 当图中有此边,直接输出
#            if (start, end) in weight:
#                return weight[(start, end)]
            # 图中没有这个点
#            if start not in graph or end not in graph:
#                return 0
            # 已经访问过
#            if start in vistied:
#                return 0
#            vistied.add(start)
#            res = 0
#            for tmp in graph[start]:
#                res = (dfs(tmp, end, vistied) * weight[(start, tmp)])
                # 只要遍历到有一个不是0的解就跳出
#                if res:
                    # 添加此边,以后访问节省时间
#                    weight[(start, end)] = res
#                    break
#            vistied.remove(start)
#            return res
#
#        res = []
#        for que in queries:
            # 用集合记录是否已经访问节点
#            tmp = dfs(que[0], que[1], set())
#            if not tmp:
#                tmp = -1.0
#            res.append(tmp)
#        return res

#并查集
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)
        res = [-1.0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.isConnected(a, b):
                res[i] = uf.value[a] / uf.value[b]
        return res

class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.value = {}
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0
    
    def find(self, x):
        root = x
        base = 1
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]
        while x != root:
            father = self.father[x]
            self.value[x] *= base
            base /= self.value[father]
            self.father[x] = root
            x = father
        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if self.find(x) != self.find(y):
            self.father[root_x] = root_y
            self.value[root_x] = self.value[y] * val / self.value[x]
    
    def isConnected(self, x, y):
        return x in self.value and y in self.value and self.find(x) == self.find(y)