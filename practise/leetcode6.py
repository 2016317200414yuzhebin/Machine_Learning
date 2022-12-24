class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [''] * numRows
        if numRows == 1:
            return s
        num = 2 * numRows -2
        for i in range(len(s)):
            if i % num >= numRows:
                res[(2 * (numRows - 1)) % (i % num)] += s[i]
            if i % num < numRows:
                res[(i % num)] += s[i]
        result = ''
        for j in res:
            result += j
        return result