class TrieNode:
    def __init__(self):
        self.children=dict()
        self.end=0

class WordDictionary:
    #use trie and dfs

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        root=self.root
        for letter in word:
            root=root.children.setdefault(letter,TrieNode())
        root.end=1

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx==len(word):
                return node.end
            
            if word[idx]==".":
                for child in node.children:
                    if dfs(node.children[child],idx+1):
                        return True
                    
            if word[idx] in node.children:
                return dfs(node.children[word[idx]],idx+1)
                
            return False
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)