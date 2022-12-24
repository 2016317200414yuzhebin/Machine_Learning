# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#递归中序遍历        
#        if root is None:
#            return []
#        else:
#            a = []
#            if self.inorderTraversal(root.left):
#                a.extend(self.inorderTraversal(root.left))
#            a.append(root.val)
#            if self.inorderTraversal(root.right):
#                a.extend(self.inorderTraversal(root.right))
#            return a

#将二叉树存储在栈中(迭代)
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                value = stack.pop()
                res.append(value.val)
                root = value.right
        return res