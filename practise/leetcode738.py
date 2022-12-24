class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        li = list(str(N))
        i = 0
        while i < len(li) - 1:
            if li[i] <= li[i + 1]:
                i += 1
            else:
                li[i] = str(int(li[i]) - 1)
                li[i + 1:] = ["9" for x in range(0, len(li) - i - 1)]
                i = 0
        return int(''.join(li))