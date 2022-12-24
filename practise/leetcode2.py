# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln = ListNode(0)
        l = ln
        flag = 0
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            value = flag + x + y
            flag = value // 10
            l.next = ListNode(value%10)
            l = l.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if flag:
            l.next = ListNode(1)
        return ln.next