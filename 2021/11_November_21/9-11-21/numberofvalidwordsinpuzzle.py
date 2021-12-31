class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        #create bitmasks for all the words and put them in counter to group similar words
        #create bitmasks for each puzzle and check if any of its submasks matches word
        #TC = O(n*avg(n)+m*2^avg(m))
        def bitmask(word):
            #func to find the bitmask of a word
            count=0
            for letter in word:
                count|=1<<(ord(letter)-ord('a'))
            return count
        
        word_map=Counter(bitmask(word) for word in words) #create bitmask counter
        ans=list()
        
        #iterate over all the puzzles
        for puzzle in puzzles:
            first=1<<(ord(puzzle[0])-ord('a')) #get first letter of puzzle in bit form
            count=word_map[first] #add words that have the first letter only
            mask=bitmask(puzzle[1:]) #bitmask of the remaining letters of the puzzle
            submask=mask
            #iterate over all the submasks
            while submask:
                count+=word_map[first|submask]
                submask=(submask-1)&mask #iterates through all the possible submasks
            ans.append(count)
        
        return ans
        
        