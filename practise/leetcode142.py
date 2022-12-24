# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#哈希
#        seen = set()
#        while head:
#            if head in seen:
#                return head
#            seen.add(head)
#            head = head.next
#        return None

#快慢指针
        if not head or not head.next:
            return None
        fast = head
        slow = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow