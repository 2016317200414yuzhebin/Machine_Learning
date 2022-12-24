class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
#桶排序
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1
        res = ''
        while len(res) < len(s):
            for i in range(26):
                if num[i]:
                    res += chr(i + ord('a'))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    res += chr(i + ord('a'))
                    num[i] -= 1
        return res