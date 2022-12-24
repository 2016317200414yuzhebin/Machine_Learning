class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack

#        while '{}' in s or '()' in s or '[]' in s:
#            s = s.replace('{}', '')
#            s = s.replace('[]', '')
#            s = s.replace('()', '')
#        return s == ''