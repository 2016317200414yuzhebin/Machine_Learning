class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for i in S:
            if i != '#':
                stack1.append(i)
            elif stack1:
                stack1.pop()
        for j in T:      
            if j != '#':
                stack2.append(j)
            elif stack2:
                stack2.pop()
        return stack1 == stack2