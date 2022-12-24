class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        ch = {}
        for i in s:
            if i in ch:
                ch[i] += 1
            else:
                ch[i] = 1
        for i in range(len(s)):
            if ch[s[i]] == 1:
                return i
        return -1