# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        Node = ListNode(-float('inf'))
        Node.next = head
        node2 = head
        while node2.next:
            node1 = Node
            if node2.val <= node2.next.val:
                node2 = node2.next
                continue
            node3 = node2.next
            node2.next = node2.next.next
            while node1.next.val < node3.val:
                node1 = node1.next
            node3.next = node1.next
            node1.next = node3
        return Node.next