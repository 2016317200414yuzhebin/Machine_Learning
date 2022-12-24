class Solution:
    def partitionLabels(self, S):
#贪心+哈希表
        map = {}
        for i, ch in enumerate(S):
            map[ch] = i # 将每个字母最后的下标存入字典中
        res = []
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, map[ch])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res