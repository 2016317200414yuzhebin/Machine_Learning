class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
#n^2超时了
#        res = -1
#        for i in range(len(gas)):
#            if gas[i] < cost[i]:
#                continue
#            flag = 0
#            left = 0
#            for j in range(i, i+len(gas)):
#                left += gas[j%len(gas)] - cost[j%len(gas)]
#                if left + gas[(j+1)%len(gas)] < cost[(j+1)%len(gas)]:
#                    break
#                flag += 1
#            if flag == len(gas):
#                res = i
#        return res

#一次遍历
        a = []
        for i in range(len(gas)):
            a.append(gas[i]-cost[i])
        if sum(a) < 0:
            return -1
        start = 0
        left = 0
        for i in range(len(a)):
            left += a[i]
            if left < 0:
                left = 0
                start = i + 1
        if start < len(a):
            return start