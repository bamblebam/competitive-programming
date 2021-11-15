from os.path import commonprefix

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c=characters
        self.l=combinationLength
        self.state=""
        
    def next(self) -> str:
        if self.state=="":
            self.state=self.c[:self.l]
        else:
            end=len(commonprefix([self.c[::-1],self.state[::-1]])) #this gets the lengh of the common prefix
            place=self.c.index(self.state[-end-1]) #this is the index of the letter in c from where the letters will be updated
            self.state=self.state[:-end-1]+self.c[place+1:place+2+end] #the first letters from the prev state + new letters
        return self.state
        
    def hasNext(self) -> bool:
        return self.state!=self.c[-self.l:] #just check if this isn't the last possible state
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()