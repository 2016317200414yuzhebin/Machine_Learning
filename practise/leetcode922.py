class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
#愚蠢的想法
#        odd = []
#        even = []
#        for i in A:
#            if i % 2 == 0:
#                even.append(i)
#            else:
#                odd.append(i)
#        j = 0
#        res = []
#        while j < len(A):
#            if j % 2 == 0:
#                res.append(even.pop())
#            else:
#                res.append(odd.pop())
#            j += 1
#        return res

#跟上面差不多
#        return [i for n in zip([i for i in A if not i % 2], [i for i in A if i % 2]) for i in n]

#双指针
        i, j = 0, 1
        while i < len(A) and j <len(A) :
            if A[i] % 2 == 0:
                i+=2
            elif A[j] % 2 == 1:
                j+=2
            else:
                A[i],A[j] = A[j],A[i]
        return A