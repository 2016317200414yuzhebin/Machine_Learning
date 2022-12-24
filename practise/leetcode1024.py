class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
#贪心算法
#        maxn = [0] * T
#        last = ret = pre = 0
#        for a, b in clips:
#            if a < T:
#                maxn[a] = max(maxn[a], b)    
#        for i in range(T):
#            last = max(last, maxn[i])
#            if i == last:
#                return -1
#            if i == pre:
#                ret += 1
#                pre = last     
#        return ret

#动态规划
        dp = [0] + [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        
        return -1 if dp[T] == float("inf") else dp[T]