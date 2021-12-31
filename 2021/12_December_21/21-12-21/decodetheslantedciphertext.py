class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        #the length of the word is row x col
        #for letter at i pos the next letter is at i+col+1 pos
        #iterate through all the cols and add letters in the above fashion till the word ends
        cols=len(encodedText)//rows
        ans=list()
        for i in range(cols):
            while i<len(encodedText):
                ans.append(encodedText[i])
                i+=cols+1
        return "".join(ans).rstrip()