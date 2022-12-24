# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#线性表
#        node = head
#        chain = []
#        l = ListNode(0)
#        node1 = l
#        while node:
#            chain.append(node)
#            node = node.next
#        for i, value in enumerate(chain[::-1]):
#            node1.next = value
#            node1 = node1.next
#            if i == len(chain) - 1:
#                node1.next = None
#        return l.next

#多元赋值的极致用法
#        node = head
#        l = None
#        while node:
#            l, l.next, node = node, l, node.next
#        return l

#递归
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node