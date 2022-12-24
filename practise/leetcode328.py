# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = head.next
        node = head.next
        while even and even.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = node
        return head