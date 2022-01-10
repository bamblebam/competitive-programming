class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        #use a set to store the sorted startwords
        #go through the targetwords, sort them and remove a letter one by one and check if they are in the set
        #do not use dict for each word it gives TLE
        lookup=set()
        for word in startWords:
            lookup.add("".join(sorted(word)))
        
        count=0
        for word in targetWords:
            t=len(word)
            word="".join(sorted(word))
            for i in range(t):
                if word[:i]+word[i+1:] in lookup:
                    count+=1
                    break
                    
        return count