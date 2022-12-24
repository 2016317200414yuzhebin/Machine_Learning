# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#快慢指针
#        slow = fast = head
#        while fast and fast.next:
#            slow = slow.next
#            fast = fast.next.next
#        return slow

#线性表
        node = head
        chain = []
        while node:
            chain.append(node)
            node = node.next
        return chain[len(chain)/2]