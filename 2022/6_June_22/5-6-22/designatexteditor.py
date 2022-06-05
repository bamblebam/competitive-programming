class TextEditor:

    def __init__(self):
        self.text=""
        self.cursor=0

    def addText(self, text: str) -> None:
        self.text=self.text[0:self.cursor]+text+self.text[self.cursor:]
        self.cursor+=len(text)
        # print(self.text,self.cursor)

    def deleteText(self, k: int) -> int:
        if k>=self.cursor:
            self.text=self.text[self.cursor:]
            tmp=self.cursor
            self.cursor=0
            # print(self.text,self.cursor)
            return tmp
        else:
            tmp=self.cursor-k
            self.text=self.text[0:tmp]+self.text[self.cursor:]
            self.cursor=tmp
            # print(self.text,self.cursor)
            return k
            
    def cursorLeft(self, k: int) -> str:
        self.cursor=max(0,self.cursor-k)
        # print(self.text,self.cursor)
        return self.text[max(self.cursor-10,0):self.cursor]

    def cursorRight(self, k: int) -> str:
        l=len(self.text)
        self.cursor=min(l,self.cursor+k)
        # print(self.text,self.cursor)
        return self.text[max(self.cursor-10,0):self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)