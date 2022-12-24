# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#迭代
        if not root:
            return root
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
#递归        
#        result = []
#        self.lastOut(result, root)
#        return result

#    def lastOut(self, result, root):
#        if root:
#            root.left = self.lastOut(result, root.left)
#            root.right = self.lastOut(result, root.right)
#            result.append(root.val)