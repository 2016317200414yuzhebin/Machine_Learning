class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t, m = '', 0
        for i in s:
            if i in t:
                m = max(m, len(t))
                t = t[t.index(i)+1:]
            t += i
        return max(m, len(t))

s = Solution()
print(s.lengthOfLongestSubstring('abcdefbghibjklmnopq'))