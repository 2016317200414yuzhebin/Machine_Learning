# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, node, value):
        if not node:
            return 0
        total = value * 10 + node.val
        if not node.left and not node.right:
            return total
        else:
            return self.dfs(node.left, total) + self.dfs(node.right, total)