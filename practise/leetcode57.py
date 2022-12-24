class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        map = {}
        for a, b in intervals:
            if a < intervals[-1][-1]:
                map[a] = b
        first = newInterval[0]
        last = newInterval[-1]
        if len(intervals) == 1:
            start, end = intervals[0][0], intervals[-1][-1]
            if first >= start and last <= end:
                return intervals
            if first < start and last > end:
                return [newInterval]
            if first >= start and first <= end and last > end:
                return [[start, last]]
            if first > end:
                return [[start, end], [first, last]]
            if first < start and last >= start and last <= end:
                return [[first, end]]
            if last < end:
                return [[first, last], [start, end]]
        start, end = intervals[0][0], intervals[0][0]
        for s in map.keys():
            if first >= s:
                start = max(start, s)
            if last >= s:
                end = max(end, s)
        res = []
        for a, b in intervals:
            if b >= first and b <= last:
                continue
            elif a >= first and a <= last:
                continue
            elif a <= first and b >= last:
                continue
            else:
                res.append([a, b])
        if first < start and last < start:
            res.append([first, last])
        elif first < start and last >= start and last <= map[start]:
            res.append([first, map[start]])
        elif first < start and last > map[start] and last < end:
            res.append([first, last])
        elif first < start and last >= end and last <=map[end]:
            res.append([first, map[end]])
        elif first < start and last > map[end]:
            res.append([first, last])
        elif first >= start and first <= map[start] and last <= map[start]:
            res.append([start, map[start]])
        elif first >= start and first <= map[start] and last > map[start] and last < end:
            res.append([start, last])
        elif first >= start and first <= map[start] and last >= end and last <= map[end]:
            res.append([start, map[end]])
        elif first >= start and first <= map[start] and last > map[end]:
            res.append([start, last])
        elif first > map[start] and first < end and last < end:
            res.append([first, last])
        elif first > map[start] and first < end and last >= end and last <= map[end]:
            res.append([first, map[end]])
        elif first > map[start] and first < end and last > map[end]:
            res.append([first, last])
        elif first >= end and first <= map[end] and last <= map[end]:
            res.append([start, map[end]])
        elif first >= end and first <= map[end] and last > map[end]:
            res.append([start, last])
        elif first > map[end]:
            res.append([first, last])
        return sorted(res)

s = Solution()
a = [[0, 5], [9, 12]]
b = [7, 16]
print(s.insert(a, b))