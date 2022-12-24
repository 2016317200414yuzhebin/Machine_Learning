# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node = head
        chain = []
        while node:
            chain.append(node)
            node = node.next
        if len(chain) > 2:
            if len(chain) % 2:
                for i, value in enumerate(chain):
                    value.next = chain[len(chain)-i-1]
                    chain[len(chain)-i-1].next = chain[i+1]
                    if i == len(chain) / 2:
                        chain[i].next = None
                        break
            else:
                for i, value in enumerate(chain):
                    if i == len(chain) / 2:
                        chain[i].next = None
                        break
                    value.next = chain[len(chain)-i-1]
                    chain[len(chain)-i-1].next = chain[i+1]