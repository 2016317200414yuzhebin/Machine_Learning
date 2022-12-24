# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nums = []
        self.medium(nums, root)
        if not len(nums):
            return True
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i-1]:
                return False
        return True
    
    def medium(self, nums, root):
        if root:
            self.medium(nums, root.left)
            nums.append(root.val)
            self.medium(nums, root.right)