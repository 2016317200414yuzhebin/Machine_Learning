class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        flag = 0
        for i, value in enumerate(A):
            if i > 0 and i < len(A)-1 and A[i-1] < value and value > A[i+1]:
                flag = i
        if not flag:
            return False
        res = True
        for i, value in enumerate(A):
            if i < flag and value >= A[i+1]:
                res = False
            if i > flag and value >= A[i-1]:
                res = False
        return res

s = Solution()
print(s.validMountainArray([0, 3, 2, 1]))