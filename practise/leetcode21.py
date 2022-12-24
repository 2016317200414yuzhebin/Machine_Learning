# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#愚蠢一点的迭代
#        node = ListNode(0)
#        l = node
#        node1 = l1
#        node2 = l2
#        while node1 and node2:
#            if node1.val <= node2.val:
#                node.next = node1
#                node1 = node1.next
#                node = node.next
#            else:
#                node.next = node2
#                node2 = node2.next
#                node = node.next
#        if node1:
#            while node1:
#                node.next = node1
#                node1 = node1.next
#                node = node.next
#        if node2:
#            while node2:
#                node.next = node2
#                node2 = node2.next
#                node = node.next
#        return l.next

#递归
#        if l1 is None:
#            return l2
#        elif l2 is None:
#            return l1
#        elif l1.val < l2.val:
#            l1.next = self.mergeTwoLists(l1.next, l2)
#            return l1
#        else:
#            l2.next = self.mergeTwoLists(l1, l2.next)
#            return l2

#迭代
        l = ListNode(0)
        node = l
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 is not None else l2
        return l.next