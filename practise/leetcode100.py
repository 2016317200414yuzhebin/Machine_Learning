# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
#邪道至尊
#        return str(p) == str(q)

        tree1 = []
        tree2 = []
        self.bfs(p, tree1)
        self.bfs(q, tree2)
        return tree1 == tree2

    def bfs(self, node, tree):
        if node:
            tree.append(node.val)
            self.bfs(node.left, tree)
            self.bfs(node.right, tree)
        else:
            tree.append("null")