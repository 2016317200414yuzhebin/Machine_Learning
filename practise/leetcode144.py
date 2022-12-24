# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#迭代
#        if not root:
#            return root
#        stack = []
#        stack.append(root)
#        res = []
#        while len(stack) > 0:
#            node = stack.pop()
#            res.append(node.val)
#            if node.right:
#                stack.append(node.right)
#            if node.left:
#                stack.append(node.left)
#        return res

#递归
        if not root:
            return root
        res = []
        self.frontSearch(root, res)
        return res

    def frontSearch(self, node, res):
        if node:
            res.append(node.val)
            self.frontSearch(node.left, res)
            self.frontSearch(node.right, res)