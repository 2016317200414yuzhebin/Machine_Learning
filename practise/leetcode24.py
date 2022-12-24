# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#递归
#        if not head or not head.next:
#            return head
#        newhead = head.next
#        head.next = self.swapPairs(newhead.next)
#        newhead.next = head
#        return newhead

#迭代
        newhead = ListNode(0)
        newhead.next = head
        temp = newhead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return newhead.next