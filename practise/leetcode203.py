# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        Node = ListNode(0)
        Node.next = head
        first = Node
        while first.next:
            if first.next.val == val:
                first.next = first.next.next
            else:
                first = first.next
        return Node.next