# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next and n == 1:
            return None
        Node = ListNode(-1)
        Node.next = head
        node = Node
        chain = []
        while node:
            chain.append(node)
            node = node.next
        if n == 1:
            chain[len(chain)-n-1].next = None
        else:
            chain[len(chain)-n-1].next = chain[len(chain)-n+1]
        return Node.next

#遍历一次
#        Node = ListNode(0, head)
#        first = head
#        second = Node
#        for i in range(n):
#            first = first.next
#        while first:
#            first = first.next
#            second = second.next        
#        second.next = second.next.next
#        return Node.next