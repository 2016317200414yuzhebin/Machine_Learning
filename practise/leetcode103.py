# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        flag = 0
        queue = []
        queue.append(root)
        while len(queue):
            res = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)
            if flag % 2 == 0:
                result.append(res)
            else:
                result.append(res[::-1])
            flag += 1
        return result