from collections import defaultdict,deque
from itertools import permutations
#not working
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList+=[beginWord]
        n,k=len(wordList),len(wordList[0])
        
        # dictionary for storing the words that belong to a certain pattern
        patterns=defaultdict(set)
        for word in wordList:
            for idx in range(k):
                patterns[word[0:idx]+'*'+word[idx+1:]].add(word)
        
        #dictionary for storing the words that can be reached from a certain word
        word_map=defaultdict(set)
        for pattern_set in patterns.values():
            for x,y in permutations(pattern_set,2):
                word_map[x].add(y)
        
        #dictionary for storing the depths of the words
        depths={w:-1 for w in wordList}
        depths[beginWord]=0
        
        #dictionary for storing paths
        paths=defaultdict(list)
        paths[beginWord]=[[beginWord]]
        queue=deque([beginWord])
        
        #bfs
        while queue:
            w=queue.popleft()
            if w==endWord:
                return paths[w]
            for word in word_map[w]:
                if depths[word]==-1 or depths[word]==depths[w]+1:
                    if depths[word]==-1:
                        queue.append(word)
                        depths[word]=depths[w]+1
                    for node in paths[w]:
                        paths[word].append(node+[word])
                    
# working        
# class Solution:
#     def findLadders(self, begW, endW, wordList):
#         wordList += [begW]
#         n, k = len(wordList), len(wordList[0])
#         patterns = defaultdict(set)
#         for word in wordList:
#             for ind in range(0, k):
#                 tmp = word[0:ind] + "*" + word[ind+1:]
#                 patterns[tmp].add(word)
                
#         G = defaultdict(set)
#         for elem in patterns.values():
#             for x, y in permutations(elem, 2):
#                 G[x].add(y)
                
#         deps = {w: -1 for w in wordList}
#         deps[begW] = 0
#         paths = defaultdict(list)
#         paths[begW] = [[begW]]
#         queue = deque([begW])

#         while queue:
#             w = queue.popleft()
#             if w == endW: return paths[w]
#             for neib in G[w]:
#                 if deps[neib] == -1 or deps[neib] == deps[w] + 1:
#                     if deps[neib] == -1:
#                         queue.append(neib)
#                         deps[neib] = deps[w] + 1
#                     for elem in paths[w]:
#                         paths[neib].append(elem + [neib])