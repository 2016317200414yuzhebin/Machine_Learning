class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        a = num / 1000
        b = (num - a * 1000) /100
        c = (num - a * 1000 - b * 100) / 10
        d = num % 10
        if a > 0:
            res += 'M' * a
        if b == 9:
            res += 'CM'
        if b >= 5 and b < 9:
            res = res + 'D' + 'C' * (b-5)
        if b == 4:
            res += 'CD'
        if b < 4 and b > 0:
            res += 'C' * b
        if c == 9:
            res += 'XC'
        if c >= 5 and c < 9:
            res = res + 'L' + 'X' * (c-5)
        if c == 4:
            res += 'XL'
        if c < 4 and c > 0:
            res += 'X' * c
        if d == 9:
            res += 'IX'
        if d < 9 and d >=5:
            res = res + 'V' + 'I' * (d-5)
        if d == 4:
            res += 'IV'
        if d < 4 and d > 0:
            res += 'I' * d
        return res

#贪心算法
#        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
#        roman_digits = ''
#        for value, symbol in digits:
#            if num == 0:
#                break
#            count, num = divmod(num, value)
#            roman_digits += symbol * count
#        return roman_digits