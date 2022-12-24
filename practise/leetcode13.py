class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        i = 0
        while i < len(s): 
            if i < len(s)-1:
                new = s[i] + s[i+1]
            else:
                new = ''
            if new in map:
                sum += map[new]
                i += 2
            else:
                value = s[i]
                sum += map[value]
                i += 1
        return sum

s = Solution()
print(s.romanToInt('MCMXCIV'))