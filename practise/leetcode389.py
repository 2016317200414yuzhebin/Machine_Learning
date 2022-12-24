class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
#        if not s:
#            return t
#        ls = list(s)
#        lt = list(t)
#        while ls:
#            ch = ls.pop(0)
#            lt.remove(ch)
#        return lt[0]

#哈希
        if not s:
            return t
        word = {}
        for ch in s:
            if ch in word:
                word[ch] += 1
            else:
                word[ch] = 1
        for ch in t:
            if ch in word:
                if word[ch]:
                    word[ch] -= 1
                else:
                    return ch
            else:
                return ch