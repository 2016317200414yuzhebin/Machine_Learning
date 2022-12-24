class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        if not s:
            return []
        res = []
        start, end = 0, 0
        while start < len(s) - 1:
            if s[start] != s[start+1]:
                start += 1
                continue
            end = start + 1
            if end == len(s) - 1:
                break
            while s[end] == s[end+1]:
                end += 1
                if end >= len(s) - 1:
                    break
            if end - start >= 2:
                res.append([start, end])
            start = end + 1
        return res