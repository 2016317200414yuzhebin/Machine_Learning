class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1])) #按前一个数由大到小，后一个数由小到大的顺序排序
        ans = []
        for person in people:
            ans.insert(person[1], person)
            print(ans)

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
s = Solution()
s.reconstructQueue(people)