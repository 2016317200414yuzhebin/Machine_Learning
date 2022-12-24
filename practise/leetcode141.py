# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#哈希
#        has = set() #无序不重复元素集
#        while head:
#            if head in has:
#                return True
#            has.add(head)
#            head = head.next
#        return False

#快慢指针
#        if head is None:
#            return False
#        fast = head
#        slow = head
#        while slow.next != None and fast.next != None:
#            fast = fast.next.next
#            if fast is None:
#                break
#            slow = slow.next
#            if fast == slow:
#                return True
#        return False

#改进后的快慢指针
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True