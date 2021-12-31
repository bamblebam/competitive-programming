class TrieNode:
    def __init__(self):
        self.children=dict()
        self.end=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        root=self.root
        for letter in word:
            root=root.children.setdefault(letter,TrieNode())
        root.end=1

class Solution:
    def dfs(self,i,j,board,node,path,res):
        if self.rem==0:
            return
        if node.end:
            res.append(path)
            self.rem-=1
            node.end=False
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        temp=board[i][j]
        if temp not in node.children:
            return
        board[i][j]='#'
        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            self.dfs(x+i,y+j,board,node.children[temp],path+temp,res)
        board[i][j]=temp
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res,trie=list(),Trie()
        self.rem=len(words)
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i,j,board,trie.root,"",res)
        return res
        