# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        node1, node2 = start, head
        nums = {}
        while node2:
            if node2.val not in nums:
                nums[node2.val] = 1
            else:
                nums[node2.val] += 1
            node2 = node2.next
        while node1.next:
            if nums[node1.next.val] != 1:
                node1.next = node1.next.next
            else:
                node1 = node1.next
        return start.next