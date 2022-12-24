# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
#        if p.val<root.val and q.val<root.val:
#            return self.lowestCommonAncestor(root.left,p,q)
#        if p.val>root.val and q.val>root.val: 
#            return self.lowestCommonAncestor(root.right,p,q)
#        return root

        path_p = self.flagSearchList(root, p)
        path_q = self.flagSearchList(root, q)
        result = None
        for i, j in zip(path_p, path_q):
            if i == j:
                result = i
            else:
                break
        return result

    def flagSearchList(self, root, flag):
        res = []
        node = root
        while node != flag:
            res.append(node)
            if flag.val < node.val:
                node = node.left
            else:
                node = node.right
        res.append(node)
        return res
