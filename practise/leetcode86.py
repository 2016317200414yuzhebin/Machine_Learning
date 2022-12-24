# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        Node = ListNode(0)
        Node.next = head
        node1, node2 = Node, Node
        while node1.next:
            if node1.next.val >= x:
                break
            node1, node2 = node1.next, node2.next
        while node2.next:
            if node2.next.val < x:
                node3 = node2.next
                node2.next, node3.next, node1.next = node3.next, node1.next, node2.next
                node1 = node1.next
                continue
            node2 = node2.next
        return Node.next