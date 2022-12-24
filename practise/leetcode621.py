class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
#26*n超时
#        if len(tasks) <= 1 or not n:
#            return len(tasks)
#        num = [0] * 26
#        for ch in tasks:
#            num[ord(ch) - ord('A')] += 1
#        flag = []
#        res = 0
#        while sum(num):
#            for i in range(26):
#                if i in flag:
#                    continue
#                max_flag = i
#            for i in range(26):
#                if i in flag:
#                    continue
#                if num[i] > num[max_flag]:
#                    max_flag = i
#            if num[max_flag]:
#                num[max_flag] -= 1
#                if len(flag) < n:
#                    flag.append(max_flag)
#                else:
#                    flag.pop(0)
#                    flag.append(max_flag)
#                res += 1
#            else:
#                if len(flag) == 0:
#                    return res
#                elif len(flag) > 0 and len(flag) < n:
#                    flag.append(-1)
#                else:
#                    flag.pop(0)
#                    flag.append(-1)
#                res += 1
#        return res

#