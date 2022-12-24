# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = ListNode(-100000)
        node.next = head
        i = head.next
        j = head
        while i:
            flag = node
            if i.val < j.val:
                while flag.next.val < i.val:
                    flag = flag.next
                j.next = i.next
                i.next = flag.next
                flag.next = i
                i = j.next
            else:
                i = i.next
                j = j.next
        return node.next