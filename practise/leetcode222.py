# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#层序遍历
#        if not root:
#            return 0
#        count = 0
#        queue = []
#        queue.append(root)
#        while len(queue):
#            node = queue.pop(0)
#            count += 1
#            if node.left:
#                queue.append(node.left)
#            if node.right:
#                queue.append(node.right)
#        return count

#递归
#        return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0

#利用完全二叉树性质
#        if not root:
#            return 0
#        l, r = self.height(root.left), self.height(root.right)
#        if l == r: # 左右子树高度相同，说明左子树必满 则节点数=左子树节点 + root节点(=1) + 递归找右子树
#            return (pow(2, l) - 1) + 1 + self.countNodes(root.right)
#        else: # 左子树比右子树高，说明右子树必满 同理
#            return (pow(2, r) - 1) + 1 + self.countNodes(root.left)
#        
#    def height(self, node):
#        h = 0
#        while node:
#            h += 1
#            node = node.left
#        return h

#二分查找
        def find(path):
            r = root
            for p in path:
                if p == '0':
                    if not r.left:  
                        return False
                    r = r.left
                else:
                    if not r.right:
                        return False
                    r = r.right
            return True

        h = 0
        p = root
        while p:
            h += 1
            p = p.left

        left, right = 2 ** (h - 1), 2 ** h - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if find(bin(mid)[3:]):
                left = mid
            else:
                right = mid - 1
        return right