# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
#暴力破解
#        valuelist = []
#        for node in lists:
#            while node:
#                valuelist.append(node.val)
#                node = node.next
#        l = ListNode(-1)
#        head = l
#        valuelist.sort()
#        for value in valuelist:
#            head.next = ListNode(value)
#            head = head.next
#        return l.next

#优先队列(堆)
#        import heapq
#        l = ListNode(0)
#        p = l
#        vallist = []
#        for node in lists:
#            while node:
#                heapq.heappush(vallist, node.val)
#                node = node.next
#        while vallist:
#            val = heapq.heappop(vallist)
#            p.next = ListNode(val)
#            p = p.next
#        return l.next

#分治算法
        n = len(lists)

        def merge(left, right):
            if left > right:
                return
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(left, mid)
            l2 = merge(mid + 1, right)
            return mergeTwoLists(l1, l2)

        def mergeTwoLists(l1, l2):
            l = ListNode(0)
            node = l
            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 if l1 is not None else l2
            return l.next

        return merge(0, n - 1)