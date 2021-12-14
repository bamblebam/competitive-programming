class Solution:
    def countVowels(self, word: str) -> int:
        #consider the substrings before the letter that have it and after the letter that have it
        #then there are left x right total substrings
        #can also be done using dp where if letter is vowel add previous dp and curr idx (no of string behind it) else just prev dp
        ans=0
        n=len(word)
        for i,x in enumerate(word):
            if x in "aeiou":
                ans+=(i+1)*(n-i)
        return ans