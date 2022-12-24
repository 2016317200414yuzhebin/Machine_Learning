# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Node = ListNode(0)
        Node.next = head
        num = 0
        add = head
        while add:
            num = num * 10 + add.val
            add = add.next
        num += 1
        p = Node
        for i in str(num):
            p.next = ListNode(int(i))
            p = p.next
        return Node.next