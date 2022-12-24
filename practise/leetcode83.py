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
#        start = ListNode(0)
#        start.next = head
#        node1, node2 = start, head
#        nums = []
#        while node2:
#            if node2.val in nums:
#                node1.next, node2 = node2.next, node2.next
#            else:
#                nums.append(node2.val)
#                node1, node2 = node1.next, node2.next
#        return head

        if not head:
            return head
        node = head
        nums = []
        nums.append(head.val)
        while node.next:
            if node.next.val in nums:
                node.next = node.next.next
            else:
                nums.append(node.next.val)
                node = node.next
        return head