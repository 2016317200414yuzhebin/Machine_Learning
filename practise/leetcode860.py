class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        money = {5 : 0, 10 : 0}
        for i in bills:
            if i == 5:
                money[5] += 1
            elif i == 10:
                money[10] += 1
                if money[5]:
                    money[5] -= 1
                else:
                    return False
            else:
                if money[10] and money[5]:
                    money[5] -= 1
                    money[10] -= 1
                elif not money[10] and money[5] >= 3:
                    money[5]  -= 3
                else:
                    return False
        return True