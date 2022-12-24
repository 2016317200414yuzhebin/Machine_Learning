class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
#厄拉多塞筛法
        if n < 3:
            return 0
        arr = [False] * n
        count = 1
        for i in range(3, n, 2):
            if not arr[i]:
                count += 1
                # 当该位是质数的时候，需要更新这个质数的所有倍数的位为1(更新时，同样跳过所有偶数倍)
                for j in range(i * i, n, 2 * i):
                    arr[j] = True
        return count