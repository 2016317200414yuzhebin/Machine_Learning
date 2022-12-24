# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#深度优先+广度优先(迭代)
#        flag = 1000000
#        queue = []
#        queue.append(root)
#        while len(queue) > 0:
#            node = queue.pop(0)
#            minright = self.minRight(node)
#            maxleft = self.maxLeft(node)
#            if minright:
#                flag = min(flag, minright - node.val)
#            if maxleft:
#                flag = min(flag, node.val - maxleft)
#            if node.left:
#                queue.append(node.left)
#            if node.right:
#                queue.append(node.right)
#        return flag
#
#    def minRight(self, node):
#        if node.right:
#            noder = node.right
#            while noder.left:
#                noder = noder.left
#            return noder.val
#
#    def maxLeft(self, node):
#        if node.left:
#            nodel = node.left
#            while nodel.right:
#                nodel = nodel.right
#            return nodel.val

#中序遍历
        res = []
        self.midOut(root, res)
        flag = 1000000
        for i, value in enumerate(res):
            if i > 0:
                flag = min(flag, value - res[i-1])
        return flag

    def midOut(self, node, res):
        if node:
            self.midOut(node.left, res)
            res.append(node.val)
            self.midOut(node.right, res)
        
#        res = []
#        def dfs(node):
#            if node:
#                dfs(node.left)
#                res.append(node.val)
#                dfs(node.right) 
#        dfs(root)
#        return min([res[i]-res[i-1] for i in range(1,len(res))])