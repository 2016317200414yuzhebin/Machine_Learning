class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
#        l = 0
#        a = []
#        y = 0
#        if x > 0:
#            while x != 0:
#                l += 1
#                n = x % 10
#                x = x // 10
#                a.append(n)
#            for i, value in enumerate(a):
#                z = value * 10 ** (l-i-1)
#                y += z
#            if y > 2**31-1:
#                return 0
#            else:
#                return y
#        elif x == 0:
#            return 0
#        else:
#            x *= -1
#            while x != 0:
#                l += 1
#                n = x % 10
#                x = x // 10
#                a.append(n)
#            for i, value in enumerate(a):
#                z = value * 10 ** (l-i-1)
#                y += z
#            y *= -1
#            if y < -2**31:
#                return 0
#            else:
#                return y
        
        
        n = 0
        if x >= 0:
            while x != 0:
                n = n*10 + x%10
                x = x / 10
            return n if n <= 2**31-1 else 0
        else:
            x *= -1
            while x != 0:
                n = n*10 + x%10
                x = x / 10
            return -n if -n >= -2**31 else 0