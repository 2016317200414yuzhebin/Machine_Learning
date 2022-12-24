import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        num = {}
        for ch in S:
            if ch in num:
                num[ch] += 1
            else:
                num[ch] = 1
            if num[ch] > (len(S) + 1) // 2:
                return ""
        res = ""
        heap = [(-x[1], x[0]) for x in num.items()] # 数值取反压入堆以实现最大堆
        heapq.heapify(heap) # 让列表具有堆特性
        while len(heap) > 1:
            _, ch1 = heapq.heappop(heap)
            _, ch2 = heapq.heappop(heap)
            res += ch1 + ch2
            num[ch1] -= 1
            num[ch2] -= 1
            if num[ch1] > 0:
                heapq.heappush(heap, (-num[ch1], ch1)) # 数值取反压入堆以实现最大堆
            if num[ch2] > 0:
                heapq.heappush(heap, (-num[ch2], ch2))
        if heap:
            res += heap[0][1]
        return res