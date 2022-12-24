# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        self.midOut(root, a)
        if a == []:
            return a
        b = dict((i, a.count(i)) for i in a)
        result = [j for j, value in b.items() if max(b.values()) == value]
        return result

    def midOut(self, root, result):
        if root:
            self.midOut(root.left, result)
            result.append(root.val)
            self.midOut(root.right, result)