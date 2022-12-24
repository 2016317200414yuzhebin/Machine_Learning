class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
#        return str(x) == str(x)[::-1]


        a = []
        a.extend(str(x))
        for i, value in enumerate(a[::-1]):
            if value != a[i]:
                return False
        return True