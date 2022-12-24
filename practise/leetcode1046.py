import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            x, y = heapq.nlargest(2, stones)
            stones.remove(x)
            stones.remove(y)
            if x != y:
                z = abs(x - y)
                stones.append(z)
        return stones[0] if stones else 0