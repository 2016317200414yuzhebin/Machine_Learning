class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
#        length, count = len(strs[0]), len(strs)
#        for i in range(length):
#            c = strs[0][i]
#            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
#                return strs[0][:i]       
#        return strs[0]

        s1 = min(strs)
        s2 = max(strs)
        for i,value in enumerate(s1):
            if value != s2[i]:
                return s2[:i]
        return s1

s = Solution()
print(s.longestCommonPrefix(["aac","a","ccc"]))