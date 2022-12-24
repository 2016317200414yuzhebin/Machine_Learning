class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
#排序
#        for i, value in enumerate(A):
#            A[i] = value ** 2
#        A.sort()
#        return A

#双指针
        n = len(A)
        negative = -1
        for i, num in enumerate(A):
            if num < 0:
                negative = i
            else:
                break

        ans = []
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(A[j] * A[j])
                j += 1
            elif j == n:
                ans.append(A[i] * A[i])
                i -= 1
            elif A[i] * A[i] < A[j] * A[j]:
                ans.append(A[i] * A[i])
                i -= 1
            else:
                ans.append(A[j] * A[j])
                j += 1

        return ans