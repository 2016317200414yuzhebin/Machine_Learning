class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num = [0] * 2001
        for i in arr:
            num[i+1000] += 1
        num.sort()
        for j, value in enumerate(num):
            if value != 0 and j > 0 and num[j] == num[j-1]:
                return False
        return True

#哈希
        num = {}
        for i in arr:
            if i in num.keys():
                num[i] += 1
            else:
                num[i] = 1
        values = {}
        for j in num:
            if num[j] in values:
                return False
            else:
                values[num[j]] = 1
        return True