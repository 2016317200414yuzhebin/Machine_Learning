class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
#递归
#        left = self.invertTree(root.left)
#        right = self.invertTree(root.right)
#        root.left, root.right = right, left
#        return root

#广度优先遍历(迭代)
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

if __name__ == "__main__":

    # 新建节点 
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)

    # 构建二叉树
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11

    # 指定 node1 为root节点
    root = node1

    s = Solution()
    s.invertTree(root)