#TrieNode is node in Trie
class TrieNode:
    def __init__(self):
        self.children=dict()
        self.endNode=0

#Trie used to store letters of words in reversed order to check if suffix exists
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        root=self.root
        for letter in word:
            root=root.children.setdefault(letter,TrieNode())
        root.endNode=1

class StreamChecker:
    #Put letters of stream in reversed order in queue and check if the suffix exists in trie
    def __init__(self, words: List[str]):
        self.words=words
        self.trie=Trie()
        self.stream=deque()
        for word in words: #putting elements in trie
            self.trie.insert(word[::-1])
        

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr=self.trie.root #the curr trie root
        for letter in self.stream: #going through all letters in stream
            if letter in curr.children: #checking if it exists in Trie
                curr=curr.children[letter]
                if curr.endNode:
                    return True
            else:
                break
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)