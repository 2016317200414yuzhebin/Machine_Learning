import collections
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
#广度优先+双向队列
#        def addWord(word):
#            if word not in wordId:
#                nonlocal nodeNum
#                wordId[word] = nodeNum
#                nodeNum += 1
#        
#        def addEdge(word):
#            addWord(word)
#            id1 = wordId[word]
#            chars = list(word)
#            for i in range(len(chars)):
#                tmp = chars[i]
#                chars[i] = "*"
#                newWord = "".join(chars)
#                addWord(newWord)
#                id2 = wordId[newWord]
#                edge[id1].append(id2)
#                edge[id2].append(id1)
#                chars[i] = tmp
#
#        if endWord not in wordList:
#            return 0  
#        wordId = {}
#        edge = collections.defaultdict(list)
#        nodeNum = 0
#        for word in wordList:
#            addEdge(word)
#        addEdge(beginWord)   
#        dis = [float("inf")] * nodeNum
#        beginId, endId = wordId[beginWord], wordId[endWord]
#        dis[beginId] = 0
#        que = collections.deque([beginId])
#        while que:
#            x = que.popleft()
#            if x == endId:
#                return dis[endId] // 2 + 1
#            for it in edge[x]:
#                if dis[it] == float("inf"):
#                    dis[it] = dis[x] + 1
#                    que.append(it)
#        return 0

#广度优先
        if endWord not in wordList:
            return 0
        l = len(endWord)     
        ws = set(wordList)
        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head
            q = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i+1:]
                        if word in tail:
                            return res + 1
                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1
        return 0