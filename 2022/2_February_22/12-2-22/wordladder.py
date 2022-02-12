class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        use BFS. The words with * can be considered as edges to the nodes which are the normal words
        create a dict and put all words that match a particular * word in its list (defaultdict)
        then go through the queue generate all * patterns of the word and iterate through all its saved words in the dict
        if a word is endword return else just add them to the list
        '''
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        
        n=len(beginWord)
        combs=defaultdict(list)
        for word in wordList:
            for i in range(n):
                combs[word[:i]+"*"+word[i+1:]].append(word)
                
        queue=deque([(beginWord,1)])
        seen={beginWord}
        
        while queue:
            curr,level=queue.popleft()
            for i in range(n):
                x=curr[:i]+"*"+curr[i+1:]
                for word in combs[x]:
                    if word==endWord:
                        return level+1
                    if word not in seen:
                        queue.append((word,level+1))
                        seen.add(word)
                combs[x]=[]
        
        return 0