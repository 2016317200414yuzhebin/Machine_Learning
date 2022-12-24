# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
#递归
#        if not root:
#            return TreeNode(val) 
#        if val < root.val:
#            root.left = self.insertIntoBST(root.left, val)
#        if val > root.val:
#            root.right = self.insertIntoBST(root.right, val) 
#        return root

        if not root:
            return TreeNode(val) 
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right   
        return root
        